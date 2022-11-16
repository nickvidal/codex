#!/usr/bin/env nix-shell
#!nix-shell -i python3 -p "python3.withPackages([])"

# Python script from https://github.com/rjzak/web_wordpuzzle

ASSETS = ( ("style", open("../../chat-web-ui/style.css", "rb").read()), ("script", open("../../chat-web-ui/script.js", "rb").read()), ("chat", open("../../chat-web-ui/index.html", "rb").read()), )

output_file = open("assets.h", "w")

for asset in ASSETS:
    name = asset[0]
    data = asset[1]
    output_file.write("const unsigned char %s[%d]= {" % (name, len(data)));
    output_file.write(",".join(["0x%02X"%x for x in data]))
    output_file.write("};\n")


output_file.close()