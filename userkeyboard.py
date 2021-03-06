from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

##replykb

button_hi = KeyboardButton('Continue!')

agree_kb = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).add(button_hi)


markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Send ur contact βοΈ', request_contact=True)
).add(
    KeyboardButton('Send ur location πΊοΈ', request_location=True)
)


##inlinepart


inline_btn_1 = InlineKeyboardButton("Author's bio", callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

inline_kb_full = InlineKeyboardMarkup().add(inline_btn_1)
inline_kb_full.add(InlineKeyboardButton('Play rock scissors paper π²', callback_data='btn2'))
inline_kb_full.add(InlineKeyboardButton('Weather π₯', callback_data='btn3'))
inline_kb_full.add(InlineKeyboardButton('Leave ur contacts π±', callback_data='btn4'))
inline_kb_full.add(InlineKeyboardButton('Share with friends β', switch_inline_query='- the best bot ever. Still for free!'))
