# -*- coding: utf-8 -*-
"""MBTI 小红书内容卡生成器（零积分 CSS，新中式视觉）
规则（老板指令）：
  - 无封面、无尾图（不要专门开头大图 / 结尾大图）
  - 标题放在每一张内容卡片页头
  - 内容只放原文，不暴露任何搬运痕迹（无「外网/爆款/播放/锚定/二创」字，落款仅「哦好MBTI」）
  - 画布靠真实正文顶对齐 + 加大字号 + 序号水印撑满
"""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

CSS = """
* { margin:0; padding:0; box-sizing:border-box; }
html,body { width:1080px; height:1440px; }
body {
  font-family:"Songti SC","STSong","SimSun","KaiTi","STKaiti",serif;
  background:
    radial-gradient(ellipse at 28% 18%, rgba(255,255,255,.55), transparent 58%),
    radial-gradient(ellipse at 82% 88%, rgba(180,140,70,.10), transparent 60%),
    linear-gradient(158deg,#f7eed9 0%, #efe1c3 52%, #e6d4af 100%);
  color:#3a2c18;
}
.card { position:relative; width:1080px; height:1440px; overflow:hidden; }
.frame {
  position:absolute; inset:34px;
  border:2px solid transparent;
  border-image:linear-gradient(135deg,#b8902f,#ecd58c,#8a6a22) 1;
  box-shadow:inset 0 0 0 6px rgba(255,255,255,.18), inset 0 0 60px rgba(150,110,50,.10);
}
.wm {
  position:absolute; right:-70px; bottom:-110px;
  font-family:"KaiTi","STKaiti",serif; font-size:780px; line-height:1;
  color:rgba(110,80,30,.05); pointer-events:none; user-select:none;
}
.seal {
  position:absolute; width:120px; height:120px; right:62px; top:62px;
  background:#9e2b25; border-radius:12px; transform:rotate(-5deg);
  display:flex; align-items:center; justify-content:center;
  color:#f3e6c8; font-family:"KaiTi","STKaiti",serif; font-size:62px;
  box-shadow:0 4px 14px rgba(120,30,20,.35);
}
.seal::before{ content:""; position:absolute; inset:7px; border:2px solid rgba(243,230,200,.55); border-radius:8px; }
.content { position:absolute; inset:96px 84px 96px 84px; display:flex; flex-direction:column; }
.mid { flex:1; display:flex; flex-direction:column; justify-content:flex-start; padding-top:10px; }
.gold {
  background:linear-gradient(135deg,#9c7b2e 0%,#ecd58c 42%,#b8902f 68%,#8a6a22 100%);
  -webkit-background-clip:text; background-clip:text; color:transparent;
}
.rule { height:3px; width:120px; margin-top:22px; background:linear-gradient(90deg,#b8902f,#ecd58c); border-radius:2px; }
/* 页头标题（每张内容卡顶部） */
.head { font-size:64px; line-height:1.2; font-weight:700; letter-spacing:2px; }
.bignum { position:absolute; left:-30px; bottom:-60px; font-family:"KaiTi","STKaiti",serif; font-size:380px; line-height:1; color:rgba(110,80,30,.05); user-select:none; pointer-events:none; }
/* 单段正文 */
.para { font-size:46px; line-height:1.78; color:#3a2c18; margin-top:30px; white-space:pre-line; }
.para.tail { font-size:40px; line-height:1.62; margin-top:28px; }
/* 多条卡（每条 = 标号 + 原文） */
.item { margin-top:30px; }
.item:first-child { margin-top:26px; }
.idx { font-size:40px; font-weight:700; letter-spacing:2px; margin-bottom:10px; }
.body { font-size:50px; line-height:1.7; color:#3a2c18; white-space:pre-line; }
.foot { position:absolute; left:84px; bottom:52px; font-size:28px; color:#8a6a35; letter-spacing:2px; }
"""

WRAP = """<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head>
<body><div class="card">
  <div class="wm">道</div>
  <div class="frame"></div>
  <div class="seal">{seal}</div>
  <div class="content">{inner}</div>
  <div class="foot">{foot}</div>
</div></body></html>"""

CONTENT = """
  <div class="head gold">{head}</div>
  <div class="rule"></div>
  <div class="bignum">{bignum}</div>
  <div class="mid">
    {body}
  </div>
"""

LI = """    <div class="item">
      <div class="idx gold">{idx}</div>
      <div class="body">{body}</div>
    </div>"""


def para_html(text, cls=""):
    return '<div class="para {}">{}</div>'.format(cls, text).replace('class="para "', 'class="para"')


def list_html(items):
    return "\n".join(LI.format(idx=a, body=b) for a, b in items)


def mk(head, bignum, body):
    return ("content", dict(head=head, bignum=bignum, body=body))


# ============ 原文（仅内容，无任何搬运痕迹字） ============
# A 组：INFJ 10 个真相
INFJ_INTRO = "INFJ 是全球约 1%–2% 的稀有类型。\n这 10 条，中一条算一条："
INFJ_TRUTHS = [
    "你是稀有物种，却总被说“看不透”。",
    "共情是天赋也是累赘——别人的情绪你能秒接，接多了自己内耗。",
    "社交完必须一个人静静，不是高冷，是去充电。",
    "一眼看穿人，靠直觉不靠逻辑，常被人问“你怎么知道”。",
    "理想主义刻进骨头里，心里有幅完美世界的图，现实总差一点。",
    "对外温和得体，真实自我只给极少数人看。",
    "最怕冲突却又最会调解，宁可自己憋着也要气氛和谐。",
    "脑子 24 小时剧场，连三年后的对话都提前预演。",
    "宁要 1 个灵魂知己，不要 100 个点赞朋友。",
    "看着柔，认准的事温柔但绝不回头。",
]
INFJ_END = "如果你边看边点头——欢迎来到 INFJ 俱乐部。\n门牌号很小，但里面的人，都很深。"

# B 组：8 个认知功能
FUNC_INTRO = "很多人以为 MBTI 就是把人塞进 16 个格子。\n但底层逻辑就一句：16 型只是壳，8 个认知功能才是魂。"
FUNCS = [
    ("Ni 内向直觉", "一眼看穿本质，靠“就是知道”而非逻辑。INFJ/INTJ 的发动机。"),
    ("Ne 外向直觉", "大脑自动发散，一个词能联想出一百种可能。ENFP/ENTP 的主场。"),
    ("Si 内向感觉", "细节和经验都存着，传统、稳定、靠谱。ISTJ/ISFJ 的底色。"),
    ("Se 外向感觉", "活在当下，五感敏锐，说走就走。ESFP/ESTP 的天赋。"),
    ("Ti 内向思考", "在自己脑子里搭逻辑，必须自洽才舒服。INTP/ISTP 的灵魂。"),
    ("Te 外向思考", "对外高效组织，目标结果导向。ENTJ/ESTJ 的刀。"),
    ("Fi 内向情感", "心里有把尺，真实比讨好重要。INFP/ISFP 的核心。"),
    ("Fe 外向情感", "天生读空气、护氛围、共情别人。ENFJ/ESFJ 的软力量。"),
]
FUNC_END = "每个人不是“拥有”某个功能，而是按 主导→辅助→第三→劣势 叠成一套功能栈。\n你的 4 个字母，本质就是这套栈的缩写。\n\nMBTI 不是“你是什么人”的标签，而是“你习惯怎么接收信息、怎么下决定”的操作系统。\n标签会贴死人，功能栈才解释得通你为什么是这样。"


def build_a():
    """无封面无尾图：开篇引言并入首卡、收尾段并入末卡。"""
    cards = []
    ch1 = [("{:02d}".format(i + 1), INFJ_TRUTHS[i]) for i in range(3)]
    ch2 = [("{:02d}".format(i + 1), INFJ_TRUTHS[i]) for i in range(3, 7)]
    ch3 = [("{:02d}".format(i + 1), INFJ_TRUTHS[i]) for i in range(7, 10)]
    cards.append(mk("INFJ 的 10 个真相", "01",
                    para_html(INFJ_INTRO) + "\n" + list_html(ch1)))
    cards.append(mk("INFJ 的 10 个真相", "02", list_html(ch2)))
    cards.append(mk("INFJ 的 10 个真相", "03",
                    list_html(ch3) + "\n" + para_html(INFJ_END, "tail")))
    return "a", "稀", cards


def build_b():
    cards = []
    cards.append(mk("8 个认知功能", "01",
                    para_html(FUNC_INTRO) + "\n" + list_html(FUNCS[:3])))
    cards.append(mk("8 个认知功能", "02", list_html(FUNCS[3:6])))
    cards.append(mk("8 个认知功能", "03",
                    list_html(FUNCS[6:]) + "\n" + para_html(FUNC_END, "tail")))
    return "b", "析", cards


def write_preview(sections):
    secs = []
    for prefix, title, n in sections:
        secs.append('<h2>{} · {} 张</h2>'.format(title, n))
        for i in range(1, n + 1):
            secs.append('<img src="{}{:02d}.png" alt="">'.format(prefix, i))
    html = """<!doctype html><html lang="zh"><head><meta charset="utf-8">
<title>MBTI 内容卡</title><style>
body{{margin:0;background:#efe6d2;color:#3a2c18;
 font-family:-apple-system,"PingFang SC","Microsoft YaHei",sans-serif;}}
.wrap{{max-width:560px;margin:0 auto;padding:18px 16px 60px;}}
.tip{{background:#fff8ea;border:1px solid #e0cfa6;border-radius:10px;
 padding:12px 16px;font-size:13px;color:#8a6a22;margin-bottom:8px;}}
h2{{font-size:19px;margin:34px 2px 12px;color:#8a6a22;
 border-left:4px solid #b8902f;padding-left:10px;letter-spacing:1px;}}
img{{width:100%;display:block;border-radius:10px;margin-bottom:14px;
 box-shadow:0 4px 16px rgba(120,90,40,.15);}}
</style></head><body><div class="wrap">
<div class="tip">MBTI 内容卡（A 组 INFJ / B 组 认知功能）· 零积分 CSS 出图</div>
{secs}
</div></body></html>""".format(secs="\n".join(secs))
    with open(os.path.join(OUT, "长页预览.html"), "w", encoding="utf-8") as f:
        f.write(html)


def main():
    sections = []
    total = 0
    for prefix, seal, cards in [build_a(), build_b()]:
        n = len(cards)
        sections.append((prefix, cards[0][1]["head"], n))
        for i, (kind, c) in enumerate(cards, 1):
            inner = CONTENT.format(head=c["head"], bignum=c["bignum"], body=c["body"])
            html = WRAP.format(css=CSS, seal=seal, foot="哦好MBTI", inner=inner)
            with open(os.path.join(OUT, "{}{:02d}.html".format(prefix, i)), "w", encoding="utf-8") as f:
                f.write(html)
            total += 1
    write_preview(sections)
    print("HTML generated:", total, "cards + preview")


if __name__ == "__main__":
    main()
