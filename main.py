from kb_v1 import KMKKeyboard

from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC
from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType

keyboard = KMKKeyboard()
keyboard.debug_enabled = True

keyboard.modules.append(Layers())
keyboard.modules.append(HoldTap())
keyboard.extensions.append(MediaKeys())

# Using drive names (KYRIAL, KYRIAR) to recognize sides; use split_side arg if you're not doing it
split = Split(split_type=SplitType.UART, use_pio=True, data_pin=keyboard.data_pin1,
              data_pin2=keyboard.data_pin2, split_target_left=False)
keyboard.modules.append(split)

ESC_LCTL = KC.HT(KC.ESC, KC.LCTL)
QUOTE_RCTL = KC.HT(KC.QUOTE, KC.RCTL)
ENT_RALT = KC.HT(KC.ENT, KC.RALT)
SPC_LALT = KC.HT(KC.SPC, KC.LALT)


keyboard.keymap = [
    [
        KC.TAB,     KC.Q,       KC.W,       KC.E,       KC.R,       KC.T,          KC.Y,       KC.U,       KC.I,       KC.O,       KC.P,      KC.BSPC,
        ESC_LCTL,   KC.A,       KC.S,       KC.D,       KC.F,       KC.G,          KC.H,       KC.J,       KC.K,       KC.L,       KC.SCLN,   QUOTE_RCTL,
        KC.LSFT,    KC.Z,       KC.X,       KC.C,       KC.V,       KC.B,          KC.N,       KC.M,       KC.COMM,    KC.DOT,     KC.SLSH,   KC.RSFT,
        KC.LGUI,    KC.SPC,   KC.MO(
            1),      KC.MOq(2),   ENT_RALT,   KC.RGUI,
    ],
    [
        KC.TAB,     KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,       KC.PGUP,    KC.HOME,    KC.UP,      KC.END,     KC.VOLU,    KC.DEL,
        ESC_LCTL,   KC.LBRC,    KC.RBRC,    KC.LCBR,    KC.RCBR,    KC.GRV,        KC.PGDN,    KC.LEFT,    KC.DOWN,    KC.RGHT,    KC.VOLD,    KC.INS,
        KC.LSFT,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,    KC.TRNS,       KC.PAUS,    KC.MPRV,    KC.MPLY,    KC.MNXT,    KC.MUTE,    KC.PSCR,
        KC.TRNS,    KC.TRNS,    KC.TRNS,       KC.TRNS,    KC.TRNS,    KC.TRNS,
    ],
    [
        KC.TAB,     KC.N1,      KC.N2,      KC.N3,      KC.N4,      KC.N5,         KC.N6,      KC.N7,      KC.N8,      KC.N9,      KC.N0,      KC.BSPC,
        ESC_LCTL,   KC.EXLM,    KC.AT,      KC.HASH,    KC.DLR,     KC.PERC,       KC.CIRC,    KC.AMPR,    KC.ASTR,    KC.LPRN,    KC.RPRN,    KC.RCTL,
        KC.LSFT,    KC.TILD,    KC.BSLS,    KC.PIPE,    KC.MINS,    KC.PLUS,       KC.EQL,     KC.UNDS,    KC.COMM,    KC.DOT,     KC.SLSH,    KC.RSFT,
        KC.TRNS,    KC.TRNS,    KC.TRNS,       KC.TRNS,    KC.TRNS,    KC.TRNS,
    ],
]


if __name__ == '__main__':
    keyboard.go()
