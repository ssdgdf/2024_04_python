# [],{},{}
# dict: key[str,int] and 중복안됨 - value :        키워드를 주면 해당 값을 준다
lecture = {
    "java":1,
    "python":2,
    "c":3,
    "javascript":4,
    # "java":5  -> 안됨
}
print(lecture["python"])

coffeeShop = {
    "starbucks":[{"name":"아메리카노","kcal":150},{"라뗴"},"민트"],
    "megacoffee":["아메리카노","라뗴","꿀아메리카노"],
}

coffeeShopMenu = {
    "starbucks" : [{"name":"아메리카노"},{"name":"라떼"}],
    "megacoffee" : [{"name":"메가리카노","price":3000},{"name":"메가라떼","price":4000}]
}
print(coffeeShopMenu["megacoffee"])
