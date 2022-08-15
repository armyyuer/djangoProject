import os


def srtread():
    file0 = open("x.srt", "r", encoding="utf-8")
    # with open("a.txt",encoding='utf8') as f:
    # content = json.load(f)
    content = file0.read()
    content = content.split('\n\n')
    print(content)
    t = ''
    for l in content:
        content2 = l.split('\n')
        t += content2[2]+"\n"

    print(t)
    file = open('srt.txt', 'wb')
    file.write(t.encode())
    file.close()

if __name__ == '__main__':
    srtread()
