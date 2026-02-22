import cv2

from camera.webcam import Webcam
from hands.hand_tracker import HandTracker
from cube_engine.cube_manager import CubeManager
from cube_engine.grid_rules import snap_to_grid
from rendering.renderer import Renderer
from config.settings import INITIAL_CUBE_SIZE

from gestures.gesture_manager import GestureManager
from frontend.menu import Menu
from frontend.ui_manager import UIManager

from gestures.custom_gestures import pinch

from utils.performance_monitor import PerformanceMonitor, SessionTimer
from analytics.heatmap import Heatmap
from frontend.construction_menu import ConstructionMenu


def init_app():
    cam = Webcam()
    tracker = HandTracker()
    renderer = Renderer()
    manager = CubeManager(INITIAL_CUBE_SIZE)
    construction_menu = ConstructionMenu()

    gesture_manager = GestureManager()
    menu = Menu()
    ui_manager = UIManager(menu, gesture_manager)

    perf_monitor = PerformanceMonitor()
    session_timer = SessionTimer()

    return (
        cam, tracker, renderer, manager,
        gesture_manager, menu, ui_manager,
        perf_monitor, session_timer, construction_menu
    )


def detect_hands(results):
    right_hand = None
    left_hand = None

    if results.multi_hand_landmarks and results.multi_handedness:
        for hand, handedness in zip(
                results.multi_hand_landmarks,
                results.multi_handedness
        ):
            label = handedness.classification[0].label
            if label == "Right":
                right_hand = hand
            elif label == "Left":
                left_hand = hand

    return right_hand, left_hand


def main():

    (
        cam, tracker, renderer, manager,
        gesture_manager, menu, ui_manager,
        perf_monitor, session_timer, construction_menu
    ) = init_app()

    cv2.namedWindow("Virtual Cube Writer", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Virtual Cube Writer", 1000, 720)

    heatmap = None

    while True:

        frame = cam.read()
        if frame is None:
            break

        h, w, _ = frame.shape

        if heatmap is None:
            heatmap = Heatmap(w, h)

        manager.size = menu.size
        manager.color = menu.selected_color

        results = tracker.process(frame)
        right_hand, left_hand = detect_hands(results)

        gesture_manager.update(left_hand, right_hand)

        # =========================
        # MENU MODE
        # =========================
        if gesture_manager.is_menu_open():

            overlay = frame.copy()
            cv2.rectangle(overlay, (0, 0), (w, h), (0, 0, 0), -1)
            cv2.addWeighted(overlay, 0.6, frame, 0.4, 0, frame)

            menu.draw(frame)
            construction_menu.draw(frame)

            if right_hand:
                index = right_hand.landmark[8]
                thumb = right_hand.landmark[4]

                ix = int(index.x * w)
                iy = int(index.y * h)
                tx = int(thumb.x * w)
                ty = int(thumb.y * h)

                if pinch((ix, iy), (tx, ty)):
                    construction_menu.handle_click(ix, iy)

            ui_manager.handle(right_hand, w, h)

        # =========================
        # DRAW / DELETE MODE
        # =========================
        else:

            if right_hand:

                index = right_hand.landmark[8]
                thumb = right_hand.landmark[4]

                ix = int(index.x * w)
                iy = int(index.y * h)
                tx = int(thumb.x * w)
                ty = int(thumb.y * h)

                gx, gy = snap_to_grid(ix, iy, manager.size)
                renderer.active_position = (gx, gy)


                # WRITE MODE
                if gesture_manager.is_write_mode(
                        left_hand, right_hand, ix, iy, tx, ty):

                    renderer.draw_hover(frame, gx, gy, manager.size)

                    if construction_menu.selected == "wall":
                        manager.build_wall(gx, gy)

                    elif construction_menu.selected == "tower":
                        manager.build_tower(gx, gy)

                    elif construction_menu.selected == "stairs":
                        manager.build_stairs(gx, gy)

                    else:
                        manager.add_cube(gx, gy)

                    heatmap.add_point(ix, iy)

                # DELETE MODE
                elif gesture_manager.is_delete_mode(
                        left_hand, right_hand, ix, iy, tx, ty):

                    for cube in manager.cubes:
                        if cube.contains(ix, iy):
                            renderer.draw_delete_hover(frame, cube)
                            manager.remove_at(ix, iy)
                            break

        # =========================
        # RENDER
        # =========================
        tracker.draw(frame, results)
        renderer.draw_cubes(frame, manager.cubes)

        fps = perf_monitor.update()
        elapsed = session_timer.get_elapsed()

        cv2.putText(frame, f"FPS: {fps}", (20, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                    (255, 255, 255), 2)

        cv2.putText(frame, f"Cubes: {len(manager.cubes)}", (20, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                    (255, 255, 255), 2)

        cv2.putText(frame, f"Time: {elapsed}s", (20, 90),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                    (255, 255, 255), 2)

        cv2.imshow("Virtual Cube Writer", frame)

        if cv2.waitKey(1) == 27:
            break

    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()