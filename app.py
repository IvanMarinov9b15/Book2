import streamlit as st

st.title("Приложение за книги")

# Създаваме масив (списък), ако още не съществува
if "books" not in st.session_state:
    st.session_state.books = []

# ==========================================
# ➕ Добавяне на книга
# ==========================================
st.header("➕ Добави книга")
title = st.text_input("Заглавие")
author = st.text_input("Автор")
price = st.number_input("Цена", min_value=0.0)

if st.button("Добави книгата"):
    book = {
        "title": title,
        "author": author,
        "price": price
    }
    st.session_state.books.append(book)
    st.success("Книгата е добавена!")

# ==========================================
# 📚 Покажи всички книги
# ==========================================
if st.button("Покажи всички книги"):
    if len(st.session_state.books) == 0:
        st.write("Няма добавени книги.")
    else:
        for book in st.session_state.books:
            st.write(f"**Заглавие:** {book['title']}")
            st.write(f"**Автор:** {book['author']}")
            st.write(f"**Цена:** {book['price']}")
            st.write("---")

# ==========================================
# 🔍 Търсене по автор (от примера)
# ==========================================
st.header("🔍 Търсене по автор")
search_author = st.text_input("Въведи име на автор")
if st.button("Търси по автор"):
    found = False
    for book in st.session_state.books:
        if book["author"].lower() == search_author.lower():
            st.write(book)
            found = True
    if not found:
        st.write("Няма намерени книги от този автор.")

# ==========================================
# 🔎 Търсене по заглавие (НОВО)
# ==========================================
st.header("🔎 Търсене по заглавие")
search_title = st.text_input("Въведи заглавие на книга")
if st.button("Търси по заглавие"):
    found = False
    for book in st.session_state.books:
        # Използваме .lower() за по-гъвкаво търсене
        if search_title.lower() in book["title"].lower():
            st.write(book)
            found = True
    if not found:
        st.write("Няма намерени книги с това заглавие.")

# ==========================================
# 💰 Търсене по цена (НОВО)
# ==========================================
st.header("💰 Търсене по цена")
max_price = st.number_input("Въведи максимална цена", min_value=0.0)
if st.button("Търси по цена"):
    found = False
    for book in st.session_state.books:
        if book["price"] <= max_price:
            st.write(book)
            found = True
    if not found:
        st.write(f"Няма книги на цена под {max_price}.")
