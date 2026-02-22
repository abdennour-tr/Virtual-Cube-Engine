from gestures.custom_gestures import is_hand_open, is_fist, pinch


class GestureManager:

    def __init__(self):
        self.menu_open = False
        self.cooldown = 0

        # Clear cooldown
        self.clear_cooldown = 0
        self.CLEAR_DELAY = 30   # nombre de frames avant réactivation

    # =========================
    # UPDATE GLOBAL
    # =========================
    def update(self, left_hand, right_hand):

        if self.cooldown > 0:
            self.cooldown -= 1

        if self.clear_cooldown > 0:
            self.clear_cooldown -= 1

        # ===== MENU =====
        if left_hand and right_hand:
            if is_hand_open(left_hand) and is_hand_open(right_hand):
                if not self.menu_open and self.cooldown == 0:
                    self.menu_open = True
                    self.cooldown = 20

    # =========================
    # STATES
    # =========================
    def is_menu_open(self):
        return self.menu_open

    def close_menu(self):
        self.menu_open = False
        self.cooldown = 20

    # =========================
    # CLEAR ALL (✊ + ✊)
    # =========================
    def is_clear_all(self, left_hand, right_hand):

        if self.menu_open:
            return False

        if not (left_hand and right_hand):
            return False

        if self.clear_cooldown > 0:
            return False

        if is_fist(left_hand) and is_fist(right_hand):
            self.clear_cooldown = self.CLEAR_DELAY
            return True

        return False

    # =========================
    # WRITE MODE (✋ + 🤏)
    # =========================
    def is_write_mode(self, left_hand, right_hand, ix, iy, tx, ty):

        if self.menu_open:
            return False

        if not (left_hand and right_hand):
            return False

        if is_hand_open(left_hand) and pinch((ix, iy), (tx, ty)):
            return True

        return False

    # =========================
    # DELETE MODE (✊ + 🤏)
    # =========================
    def is_delete_mode(self, left_hand, right_hand, ix, iy, tx, ty):

        if self.menu_open:
            return False

        if not (left_hand and right_hand):
            return False

        if is_fist(left_hand) and pinch((ix, iy), (tx, ty)):
            return True

        return False