color_code = {"black": "#000000", "bone": "#e3dac9", "cream": "#fffdd0", "gray": "#bebebe","iris":"#5a4fcf"}
color = input("Color you choose: ").lower()
while color != "":
    while color not in color_code:
      print("Please try agin")
      color = input(">>>")
    print(color_code.get(color))
    color = input(">>>")
print("Thanks!")

