from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

##replykb

button_hi = KeyboardButton('Continue!')

agree_kb = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True
).add(button_hi)


markup_request = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton('Send ur contact ☎️', request_contact=True)
).add(
    KeyboardButton('Send ur location 🗺️', request_location=True)
)


##inlinepart


inline_btn_1 = InlineKeyboardButton("Author's bio", callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)

inline_kb_full = InlineKeyboardMarkup().add(inline_btn_1)
inline_kb_full.add(InlineKeyboardButton('Play rock scissors paper 🎲', callback_data='btn2'))
inline_kb_full.add(InlineKeyboardButton('Weather 🌥', callback_data='btn3'))
inline_kb_full.add(InlineKeyboardButton('Leave ur contacts 📱', callback_data='btn4'))
inline_kb_full.add(InlineKeyboardButton('Share with friends ✅', switch_inline_query='- the best bot ever. Still for free!'))
