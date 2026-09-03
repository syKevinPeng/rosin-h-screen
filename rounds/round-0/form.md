# Atom audit / 原子审核 · round 0: incumbent atoms / 第 0 轮：现有原子

**form version / 表格版本:** `cf35edf19d24` · **rater / 评分人:** ☐ the violinist / 小提琴老师 · ☐ the author (Siyuan) / 作者（思远）

Printable form (paper fallback): cards in fixed order, tick one box per question. / 打印版（纸质备用）：卡片按固定顺序排列，每题勾选一个方框。

You will see 27 short cards. Each describes one thing our system measures from a violin performance (an "atom"). For each card answer two questions and, if you like, leave a note. There are no right answers; we want your judgment as a teacher. About 25 to 35 minutes.

下面有 27 张卡片，每张描述我们的系统从小提琴演奏中测量的一项内容（一个“原子”）。请对每张卡片回答两个问题，也可以留言。没有标准答案，我们需要的是您作为老师的判断。大约需要 25 到 35 分钟。

## The two questions / 两个问题

**H1.** Is this something violin teachers actually attend to in lessons? / 小提琴老师在课上真的会关注这一点吗？

**H2.** If a tutor reported this value to a student, could the student act on it? / 如果辅导系统把这个数值报告给学生，学生能据此做出调整吗？  
*The number itself, not the concept: for example "your bow speed varied a lot in this phrase", as opposed to a quantity that no instruction maps to. / 指的是数值本身，而不是概念：例如“这一句里你的弓速变化很大”，相对于一个无法转化为任何练习指令的量。*

## The scale (no midpoint, on purpose) / 评分标准（有意不设中间值）

- **1** clearly no / 明显不是
- **2** probably no / 可能不是
- **3** probably yes / 可能是
- **4** clearly yes / 明显是

---

### 1. Bow speed, with direction / 弓速（含方向）
`bow_speed`  
**Calibration example: rate it like any other card. / 校准示例：请像对待其他卡片一样评分。**

**How teachers say it / 老师的说法:**
- bow speed · attributed to / 转述自: Fischer, The Violin Lesson (2013); Flesch, The Art of Violin Playing, Book 1
- It is impossible to scratch if the bow keeps moving · quoted / 原文引用: Fischer, The Violin Lesson (2013), chapter heading
- 匀、准、美 · quoted / 原文引用: 林耀基 口诀，见 杨宝智《林耀基小提琴教学法精要》(2004)
- 弓速 · paraphrase, uncited / 转述，未引用

**What it measures / 测量内容:** How fast the bow is moving along the string, with the sign showing whether it is a down-bow or an up-bow. / 弓沿弦运动的速度，正负号表示下弓还是上弓。  
**Unit / 单位:** bow-hair lengths per second, so 1 means a whole bow in one second / 每秒多少个弓长，1 表示一秒拉完一整弓  
**Range / 取值范围:** 0 = bow stopped; positive = down-bow (toward the tip); negative = up-bow / 0 = 弓静止；正值 = 下弓（向弓尖）；负值 = 上弓

**H1.** Is this something violin teachers actually attend to in lessons? / 小提琴老师在课上真的会关注这一点吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**H2.** If a tutor reported this value to a student, could the student act on it? / 如果辅导系统把这个数值报告给学生，学生能据此做出调整吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**Notes (optional): how would you say this to a student? Anything unclear? / 备注（选填）：您会怎样对学生说这一点？有不清楚的地方吗？**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 2. Right-wrist rotation, model axis Z, relative to the player's usual / 右手腕转动，模型 Z 轴（相对于演奏者本次的习惯姿势）
`right_wrist_aa_z_dev_deg`  
**Calibration example: rate it like any other card. / 校准示例：请像对待其他卡片一样评分。**

**How teachers say it / 老师的说法:**
- bent wrist · attributed to / 转述自: Rolland, The Teaching of Action in String Playing (1974)
- wrist flexion at the frog · expert spreadsheet / 专家表格: ViolinITS schema leaf
- how the wrist is turned about the model's Z axis · paraphrase, uncited / 转述，未引用
- 手腕弯曲 / 手腕的转动 · paraphrase, uncited / 转述，未引用

**What it measures / 测量内容:** One of three parts of how the bow-hand wrist is turned, taken about the motion-capture model's Z axis, compared with this player's usual wrist posture in that recording. The three axes are the model's axes, not anatomical names such as flexion or deviation. / 持弓手手腕转动的三个分量之一，取动作捕捉模型 Z 轴方向，与演奏者在这次录音中惯常的手腕姿势相比较。三个轴是模型的坐标轴，不是屈伸、偏斜等解剖学名称。  
**Unit / 单位:** degrees / 度  
**Range / 取值范围:** 0 = the player's usual wrist posture in the recording; positive or negative = turned one way or the other about that axis / 0 = 演奏者本次惯常的手腕姿势；正或负 = 绕该轴向一侧或另一侧转动

**H1.** Is this something violin teachers actually attend to in lessons? / 小提琴老师在课上真的会关注这一点吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**H2.** If a tutor reported this value to a student, could the student act on it? / 如果辅导系统把这个数值报告给学生，学生能据此做出调整吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**Notes (optional): how would you say this to a student? Anything unclear? / 备注（选填）：您会怎样对学生说这一点？有不清楚的地方吗？**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 3. Contact point, relative to the player's usual / 触弦点（相对于演奏者本次的习惯位置）
`contact_bridge_ratio_dev`

**How teachers say it / 老师的说法:**
- soundpoint / the five soundpoints · attributed to / 转述自: Fischer, The Violin Lesson (2013)
- contact point · attributed to / 转述自: Flesch, The Art of Violin Playing, Book 1
- the bow drifting from the contact point · attributed to / 转述自: Starr, The Suzuki Violinist
- 匀 · quoted / 原文引用: 林耀基 口诀，见 杨宝智《林耀基小提琴教学法精要》(2004)
- 触弦点 / 弓与弦的接触点 · paraphrase, uncited / 转述，未引用

**What it measures / 测量内容:** Where the bow hair touches the string between the bridge and the fingerboard, compared with the player's own usual contact point in that recording. / 弓毛在琴马与指板之间触弦的位置，与演奏者在这次录音中自己惯常的触弦点相比较。  
**Unit / 单位:** a fraction of the string length (bridge to nut) / 弦长（琴马到琴枕）的比例  
**Range / 取值范围:** 0 = the player's usual point; negative = closer to the bridge than usual; positive = closer to the fingerboard than usual / 0 = 惯常位置；负值 = 比平时更靠近琴马；正值 = 比平时更靠近指板

**H1.** Is this something violin teachers actually attend to in lessons? / 小提琴老师在课上真的会关注这一点吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**H2.** If a tutor reported this value to a student, could the student act on it? / 如果辅导系统把这个数值报告给学生，学生能据此做出调整吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**Notes (optional): how would you say this to a student? Anything unclear? / 备注（选填）：您会怎样对学生说这一点？有不清楚的地方吗？**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 4. Position along the bow, frog to tip / 弓段位置（弓根到弓尖）
`hair_pos`

**How teachers say it / 老师的说法:**
- at the frog / in the middle / at the tip · paraphrase, uncited / 转述，未引用
- bow distribution · expert spreadsheet / 专家表格: ViolinITS etude classification spreadsheet, columns "Equal length, 2 bow length, 3-4 bow length"
- whole bows · attributed to / 转述自: Fischer, The Violin Lesson (2013)
- 弓根 / 中弓 / 弓尖；分弓段 · paraphrase, uncited / 转述，未引用

**What it measures / 测量内容:** Which part of the bow hair is on the string at that moment, from the frog to the tip. / 此刻弓毛的哪一段在弦上，从弓根到弓尖。  
**Unit / 单位:** a fraction of the bow-hair length / 弓毛全长的比例  
**Range / 取值范围:** 0 = at the frog; 0.5 = the middle of the bow; 1 = at the tip / 0 = 弓根；0.5 = 中弓；1 = 弓尖

**H1.** Is this something violin teachers actually attend to in lessons? / 小提琴老师在课上真的会关注这一点吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**H2.** If a tutor reported this value to a student, could the student act on it? / 如果辅导系统把这个数值报告给学生，学生能据此做出调整吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**Notes (optional): how would you say this to a student? Anything unclear? / 备注（选填）：您会怎样对学生说这一点？有不清楚的地方吗？**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 5. Bow-to-string gap, on or off the string / 弓毛与弦的距离（贴弦或离弦）
`hair_string_gap_ratio`

**How teachers say it / 老师的说法:**
- bow on the string / off the string · paraphrase, uncited / 转述，未引用
- Sautillé & Spiccato, Ricochet, Flying staccato (off-string strokes) · expert spreadsheet / 专家表格: ViolinITS etude classification spreadsheet
- 贴弦 / 离弦；跳弓 · paraphrase, uncited / 转述，未引用

**What it measures / 测量内容:** How far the bow hair is from the string: zero when the bow is on the string, larger when it is lifted off. / 弓毛离弦有多远：弓贴弦时为零，抬起时变大。  
**Unit / 单位:** a fraction of the string length / 弦长的比例  
**Range / 取值范围:** 0 = hair on the string; larger = further off the string / 0 = 弓毛贴弦；越大 = 离弦越远

**H1.** Is this something violin teachers actually attend to in lessons? / 小提琴老师在课上真的会关注这一点吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**H2.** If a tutor reported this value to a student, could the student act on it? / 如果辅导系统把这个数值报告给学生，学生能据此做出调整吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**Notes (optional): how would you say this to a student? Anything unclear? / 备注（选填）：您会怎样对学生说这一点？有不清楚的地方吗？**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 6. Bow skew: straight versus crooked bow / 弓的偏斜角（运弓直不直）
`skew_deg`

**How teachers say it / 老师的说法:**
- crooked bow · attributed to / 转述自: Hamann & Gillespie, Strategies for Teaching Strings (4th ed., 2018)
- keep the bow straight · paraphrase, uncited / 转述，未引用
- bow–string angle · measurement study / 实验研究: Provenzale et al. (2024), Sensors
- 运弓要直 / 弓走直线 · paraphrase, uncited / 转述，未引用

**What it measures / 测量内容:** How far the bow is from being at a right angle to the string, that is, how crooked the bow is. / 弓偏离与弦垂直的程度，也就是运弓有多“歪”。  
**Unit / 单位:** degrees / 度  
**Range / 取值范围:** 0 = perfectly straight bow; larger = more crooked, whichever way it leans / 0 = 完全垂直于弦（弓走直线）；越大 = 越歪，不分方向

**H1.** Is this something violin teachers actually attend to in lessons? / 小提琴老师在课上真的会关注这一点吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**H2.** If a tutor reported this value to a student, could the student act on it? / 如果辅导系统把这个数值报告给学生，学生能据此做出调整吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**Notes (optional): how would you say this to a student? Anything unclear? / 备注（选填）：您会怎样对学生说这一点？有不清楚的地方吗？**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 7. Bow tilt around the string: which string the bow is on / 弓绕弦的倾角（弓靠向哪根弦）
`string_side_deg`

**How teachers say it / 老师的说法:**
- string crossing · attributed to / 转述自: Galamian, Principles of Violin Playing and Teaching (1962); Rolland, The Teaching of Action in String Playing (1974)
- bow tilt · measurement study / 实验研究: Provenzale et al. (2024), Sensors
- string level · paraphrase, uncited / 转述，未引用
- 换弦角度 / 弦平面 · paraphrase, uncited / 转述，未引用

**What it measures / 测量内容:** The angle at which the bow sits around the string, which shows which string the bow is leaning toward, measured against the violin body. / 弓绕着弦所处的角度，反映弓靠向哪根弦，以琴身为参照。  
**Unit / 单位:** degrees / 度  
**Range / 取值范围:** an angle; smaller toward the G-string side, larger toward the E-string side / 角度；越靠 G 弦一侧越小，越靠 E 弦一侧越大

**H1.** Is this something violin teachers actually attend to in lessons? / 小提琴老师在课上真的会关注这一点吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**H2.** If a tutor reported this value to a student, could the student act on it? / 如果辅导系统把这个数值报告给学生，学生能据此做出调整吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**Notes (optional): how would you say this to a student? Anything unclear? / 备注（选填）：您会怎样对学生说这一点？有不清楚的地方吗？**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 8. Bow speed, with direction / 弓速（含方向）
`bow_speed`

**How teachers say it / 老师的说法:**
- bow speed · attributed to / 转述自: Fischer, The Violin Lesson (2013); Flesch, The Art of Violin Playing, Book 1
- It is impossible to scratch if the bow keeps moving · quoted / 原文引用: Fischer, The Violin Lesson (2013), chapter heading
- 匀、准、美 · quoted / 原文引用: 林耀基 口诀，见 杨宝智《林耀基小提琴教学法精要》(2004)
- 弓速 · paraphrase, uncited / 转述，未引用

**What it measures / 测量内容:** How fast the bow is moving along the string, with the sign showing whether it is a down-bow or an up-bow. / 弓沿弦运动的速度，正负号表示下弓还是上弓。  
**Unit / 单位:** bow-hair lengths per second, so 1 means a whole bow in one second / 每秒多少个弓长，1 表示一秒拉完一整弓  
**Range / 取值范围:** 0 = bow stopped; positive = down-bow (toward the tip); negative = up-bow / 0 = 弓静止；正值 = 下弓（向弓尖）；负值 = 上弓

**H1.** Is this something violin teachers actually attend to in lessons? / 小提琴老师在课上真的会关注这一点吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**H2.** If a tutor reported this value to a student, could the student act on it? / 如果辅导系统把这个数值报告给学生，学生能据此做出调整吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**Notes (optional): how would you say this to a student? Anything unclear? / 备注（选填）：您会怎样对学生说这一点？有不清楚的地方吗？**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 9. Bow speed: how fast, regardless of direction / 弓速（只看快慢，不分方向）
`bow_speed_abs`

**How teachers say it / 老师的说法:**
- bow speed · attributed to / 转述自: Fischer, The Violin Lesson (2013); Flesch, The Art of Violin Playing, Book 1
- the bow keeps moving · quoted / 原文引用: Fischer, The Violin Lesson (2013), chapter heading
- 弓速 · paraphrase, uncited / 转述，未引用

**What it measures / 测量内容:** How fast the bow is moving, regardless of whether it is a down-bow or an up-bow. / 弓运动有多快，不区分上弓下弓。  
**Unit / 单位:** bow-hair lengths per second / 每秒多少个弓长  
**Range / 取值范围:** 0 = stopped; 1 = a whole bow in one second; larger = faster / 0 = 静止；1 = 一秒拉完一整弓；越大越快

**H1.** Is this something violin teachers actually attend to in lessons? / 小提琴老师在课上真的会关注这一点吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**H2.** If a tutor reported this value to a student, could the student act on it? / 如果辅导系统把这个数值报告给学生，学生能据此做出调整吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**Notes (optional): how would you say this to a student? Anything unclear? / 备注（选填）：您会怎样对学生说这一点？有不清楚的地方吗？**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 10. Bow acceleration / 弓的加速度
`bow_accel`

**How teachers say it / 老师的说法:**
- speeding up or slowing down the bow within a stroke · paraphrase, uncited / 转述，未引用
- Martelé & Marcato, Accent (accented strokes) · expert spreadsheet / 专家表格: ViolinITS etude classification spreadsheet
- 弓速变化 / 加速、减速 · paraphrase, uncited / 转述，未引用

**What it measures / 测量内容:** How quickly the bow is speeding up or slowing down within a stroke. / 在一弓之内，弓速变快或变慢的快慢程度。  
**Unit / 单位:** change in bow speed per second / 弓速每秒的变化量  
**Range / 取值范围:** 0 = steady speed; larger = the speed is changing faster; the sign follows the down-bow-positive convention / 0 = 匀速；越大 = 速度变化越快；正负与“下弓为正”一致

**H1.** Is this something violin teachers actually attend to in lessons? / 小提琴老师在课上真的会关注这一点吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**H2.** If a tutor reported this value to a student, could the student act on it? / 如果辅导系统把这个数值报告给学生，学生能据此做出调整吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**Notes (optional): how would you say this to a student? Anything unclear? / 备注（选填）：您会怎样对学生说这一点？有不清楚的地方吗？**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 11. Bow direction: down-bow or up-bow / 运弓方向（下弓或上弓）
`direction_sign`

**How teachers say it / 老师的说法:**
- down-bow / up-bow · paraphrase, uncited / 转述，未引用
- 下弓 / 上弓 · paraphrase, uncited / 转述，未引用

**What it measures / 测量内容:** Whether the bow is moving as a down-bow or an up-bow, as a smooth value that passes through zero when the bow changes direction. / 弓正在下弓还是上弓，用一个连续的软符号表示，换弓时经过零。  
**Unit / 单位:** a sign from −1 to +1 / −1 到 +1 之间的符号值  
**Range / 取值范围:** +1 = clearly down-bow; −1 = clearly up-bow; near 0 = stopped or changing direction / +1 = 明确的下弓；−1 = 明确的上弓；接近 0 = 静止或正在换弓

**H1.** Is this something violin teachers actually attend to in lessons? / 小提琴老师在课上真的会关注这一点吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**H2.** If a tutor reported this value to a student, could the student act on it? / 如果辅导系统把这个数值报告给学生，学生能据此做出调整吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**Notes (optional): how would you say this to a student? Anything unclear? / 备注（选填）：您会怎样对学生说这一点？有不清楚的地方吗？**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 12. Right elbow bend (bow arm) / 右臂肘部弯曲（持弓手臂）
`right_elbow_flexion_deg`

**How teachers say it / 老师的说法:**
- elbow angle / elbow height of the bow arm · paraphrase, uncited / 转述，未引用
- whole-arm strokes · attributed to / 转述自: Rolland, The Teaching of Action in String Playing (1974); Galamian, Principles (1962)
- changing notes without changing the arm shape · attributed to / 转述自: 林耀基，见 杨宝智 (2004)（合集中仅有英文转述，未录原文）
- 右肘的高低 / 肘部弯曲 · paraphrase, uncited / 转述，未引用

**What it measures / 测量内容:** How much the bow-arm elbow is bent, measured from the motion-capture model's straight-arm reference. / 持弓手臂肘部弯曲的程度，以动作捕捉模型的伸直手臂为参照。  
**Unit / 单位:** degrees of rotation from the reference pose, not a clinically calibrated joint angle / 相对参考姿势的旋转度数，不是临床标定的关节角  
**Range / 取值范围:** 0 = arm straight in the reference pose; larger = more bent / 0 = 参考姿势中的伸直手臂；越大 = 弯曲越多

**H1.** Is this something violin teachers actually attend to in lessons? / 小提琴老师在课上真的会关注这一点吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**H2.** If a tutor reported this value to a student, could the student act on it? / 如果辅导系统把这个数值报告给学生，学生能据此做出调整吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**Notes (optional): how would you say this to a student? Anything unclear? / 备注（选填）：您会怎样对学生说这一点？有不清楚的地方吗？**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 13. Right-wrist rotation, model axis X, relative to the player's usual / 右手腕转动，模型 X 轴（相对于演奏者本次的习惯姿势）
`right_wrist_aa_x_dev_deg`

**How teachers say it / 老师的说法:**
- bent wrist · attributed to / 转述自: Rolland, The Teaching of Action in String Playing (1974)
- wrist flexion at the frog · expert spreadsheet / 专家表格: ViolinITS schema leaf
- how the wrist is turned about the model's X axis · paraphrase, uncited / 转述，未引用
- 手腕弯曲 / 手腕的转动 · paraphrase, uncited / 转述，未引用

**What it measures / 测量内容:** One of three parts of how the bow-hand wrist is turned, taken about the motion-capture model's X axis, compared with this player's usual wrist posture in that recording. The three axes are the model's axes, not anatomical names such as flexion or deviation. / 持弓手手腕转动的三个分量之一，取动作捕捉模型 X 轴方向，与演奏者在这次录音中惯常的手腕姿势相比较。三个轴是模型的坐标轴，不是屈伸、偏斜等解剖学名称。  
**Unit / 单位:** degrees / 度  
**Range / 取值范围:** 0 = the player's usual wrist posture in the recording; positive or negative = turned one way or the other about that axis / 0 = 演奏者本次惯常的手腕姿势；正或负 = 绕该轴向一侧或另一侧转动

**H1.** Is this something violin teachers actually attend to in lessons? / 小提琴老师在课上真的会关注这一点吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**H2.** If a tutor reported this value to a student, could the student act on it? / 如果辅导系统把这个数值报告给学生，学生能据此做出调整吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**Notes (optional): how would you say this to a student? Anything unclear? / 备注（选填）：您会怎样对学生说这一点？有不清楚的地方吗？**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 14. Right-wrist rotation, model axis Y, relative to the player's usual / 右手腕转动，模型 Y 轴（相对于演奏者本次的习惯姿势）
`right_wrist_aa_y_dev_deg`

**How teachers say it / 老师的说法:**
- bent wrist · attributed to / 转述自: Rolland, The Teaching of Action in String Playing (1974)
- wrist flexion at the frog · expert spreadsheet / 专家表格: ViolinITS schema leaf
- how the wrist is turned about the model's Y axis · paraphrase, uncited / 转述，未引用
- 手腕弯曲 / 手腕的转动 · paraphrase, uncited / 转述，未引用

**What it measures / 测量内容:** One of three parts of how the bow-hand wrist is turned, taken about the motion-capture model's Y axis, compared with this player's usual wrist posture in that recording. The three axes are the model's axes, not anatomical names such as flexion or deviation. / 持弓手手腕转动的三个分量之一，取动作捕捉模型 Y 轴方向，与演奏者在这次录音中惯常的手腕姿势相比较。三个轴是模型的坐标轴，不是屈伸、偏斜等解剖学名称。  
**Unit / 单位:** degrees / 度  
**Range / 取值范围:** 0 = the player's usual wrist posture in the recording; positive or negative = turned one way or the other about that axis / 0 = 演奏者本次惯常的手腕姿势；正或负 = 绕该轴向一侧或另一侧转动

**H1.** Is this something violin teachers actually attend to in lessons? / 小提琴老师在课上真的会关注这一点吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**H2.** If a tutor reported this value to a student, could the student act on it? / 如果辅导系统把这个数值报告给学生，学生能据此做出调整吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**Notes (optional): how would you say this to a student? Anything unclear? / 备注（选填）：您会怎样对学生说这一点？有不清楚的地方吗？**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 15. Right-wrist rotation, model axis Z, relative to the player's usual / 右手腕转动，模型 Z 轴（相对于演奏者本次的习惯姿势）
`right_wrist_aa_z_dev_deg`

**How teachers say it / 老师的说法:**
- bent wrist · attributed to / 转述自: Rolland, The Teaching of Action in String Playing (1974)
- wrist flexion at the frog · expert spreadsheet / 专家表格: ViolinITS schema leaf
- how the wrist is turned about the model's Z axis · paraphrase, uncited / 转述，未引用
- 手腕弯曲 / 手腕的转动 · paraphrase, uncited / 转述，未引用

**What it measures / 测量内容:** One of three parts of how the bow-hand wrist is turned, taken about the motion-capture model's Z axis, compared with this player's usual wrist posture in that recording. The three axes are the model's axes, not anatomical names such as flexion or deviation. / 持弓手手腕转动的三个分量之一，取动作捕捉模型 Z 轴方向，与演奏者在这次录音中惯常的手腕姿势相比较。三个轴是模型的坐标轴，不是屈伸、偏斜等解剖学名称。  
**Unit / 单位:** degrees / 度  
**Range / 取值范围:** 0 = the player's usual wrist posture in the recording; positive or negative = turned one way or the other about that axis / 0 = 演奏者本次惯常的手腕姿势；正或负 = 绕该轴向一侧或另一侧转动

**H1.** Is this something violin teachers actually attend to in lessons? / 小提琴老师在课上真的会关注这一点吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**H2.** If a tutor reported this value to a student, could the student act on it? / 如果辅导系统把这个数值报告给学生，学生能据此做出调整吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**Notes (optional): how would you say this to a student? Anything unclear? / 备注（选填）：您会怎样对学生说这一点？有不清楚的地方吗？**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 16. Right shoulder rotation, relative to the player's usual / 右肩转动（相对于演奏者本次的习惯姿势）
`right_shoulder_rotation_dev_deg`

**How teachers say it / 老师的说法:**
- raised shoulder · attributed to / 转述自: Rolland, The Teaching of Action in String Playing (1974)
- gripping / clamping · attributed to / 转述自: Havas, A New Approach to Violin Playing (1961)
- 让琴成为身体的一部分 · quoted / 原文引用: 林耀基，见 杨宝智《林耀基小提琴教学法精要》(2004)
- 耸肩 / 肩膀抬起 · paraphrase, uncited / 转述，未引用

**What it measures / 测量内容:** How much the bow-arm shoulder is turned, compared with this player's usual shoulder position in that recording, in any direction. / 持弓手臂肩关节的转动量，与演奏者在这次录音中惯常的肩部姿势相比较，不分方向。  
**Unit / 单位:** degrees of rotation, not a clinically calibrated joint angle / 旋转度数，不是临床标定的关节角  
**Range / 取值范围:** 0 = the usual shoulder position; larger = further from it / 0 = 惯常的肩部姿势；越大 = 偏离越多

**H1.** Is this something violin teachers actually attend to in lessons? / 小提琴老师在课上真的会关注这一点吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**H2.** If a tutor reported this value to a student, could the student act on it? / 如果辅导系统把这个数值报告给学生，学生能据此做出调整吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**Notes (optional): how would you say this to a student? Anything unclear? / 备注（选填）：您会怎样对学生说这一点？有不清楚的地方吗？**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 17. Head and neck tilt / 头颈倾斜
`neck_tilt_deg`

**How teachers say it / 老师的说法:**
- head position / head tilt · paraphrase, uncited / 转述，未引用
- chin / jaw pressure · expert spreadsheet / 专家表格: ViolinITS schema leaf
- 小提琴学习中常见错误姿势的分析与纠正 · quoted / 原文引用: 杨凌超 (2001)，文章标题
- 头的位置 / 歪头 · paraphrase, uncited / 转述，未引用

**What it measures / 测量内容:** How far the head and neck are tilted away from the motion-capture model's upright reference, in any direction. / 头颈相对于动作捕捉模型直立参考姿势的倾斜程度，不分方向。  
**Unit / 单位:** degrees / 度  
**Range / 取值范围:** 0 = the upright reference; larger = more tilted / 0 = 直立参考姿势；越大 = 倾斜越多

**H1.** Is this something violin teachers actually attend to in lessons? / 小提琴老师在课上真的会关注这一点吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**H2.** If a tutor reported this value to a student, could the student act on it? / 如果辅导系统把这个数值报告给学生，学生能据此做出调整吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**Notes (optional): how would you say this to a student? Anything unclear? / 备注（选填）：您会怎样对学生说这一点？有不清楚的地方吗？**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 18. Spine curvature: upright versus slouched / 脊柱弯曲（挺直还是弯腰驼背）
`spine_curvature_deg`

**How teachers say it / 老师的说法:**
- posture · attributed to / 转述自: Kreitman, Teaching from the Balance Point (1998); Flesch, The Art of Violin Playing, Book 1; Gruenberg (1919)
- balanced stance · attributed to / 转述自: Rolland, The Teaching of Action in String Playing (1974)
- slouching · paraphrase, uncited / 转述，未引用
- 姿势 / 站姿 / 挺直 · paraphrase, uncited / 转述，未引用

**What it measures / 测量内容:** How far the upper body is bent away from the motion-capture model's upright reference, combining the three spine joints. / 上身相对于动作捕捉模型直立参考姿势的弯曲程度，综合三个脊柱关节。  
**Unit / 单位:** degrees / 度  
**Range / 取值范围:** 0 = the upright reference; larger = more curved / 0 = 直立参考姿势；越大 = 弯曲越多

**H1.** Is this something violin teachers actually attend to in lessons? / 小提琴老师在课上真的会关注这一点吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**H2.** If a tutor reported this value to a student, could the student act on it? / 如果辅导系统把这个数值报告给学生，学生能据此做出调整吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**Notes (optional): how would you say this to a student? Anything unclear? / 备注（选填）：您会怎样对学生说这一点？有不清楚的地方吗？**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 19. Violin hold height / 持琴高度
`violin_hold_height_ratio`

**How teachers say it / 老师的说法:**
- scroll drooping · attributed to / 转述自: Auer, Violin Playing as I Teach It (1921)
- violin drifting over the right arm · attributed to / 转述自: Starr, The Suzuki Violinist
- instrument support · attributed to / 转述自: Rolland, The Teaching of Action in String Playing (1974)
- 让琴成为身体的一部分 · quoted / 原文引用: 林耀基，见 杨宝智《林耀基小提琴教学法精要》(2004)
- 琴头下垂 / 持琴高度 · paraphrase, uncited / 转述，未引用

**What it measures / 测量内容:** How high the violin's bridge sits above the player's hips, so a drooping violin gives a smaller value and a well-raised one a larger value. / 琴马相对于演奏者髋部的高度：琴头下垂时数值变小，持琴较高时数值变大。  
**Unit / 单位:** a fraction of the string length, so it does not depend on body size / 弦长的比例，因此不受身材大小影响  
**Range / 取值范围:** larger = the violin is held higher relative to the hips / 越大 = 相对髋部持琴越高

**H1.** Is this something violin teachers actually attend to in lessons? / 小提琴老师在课上真的会关注这一点吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**H2.** If a tutor reported this value to a student, could the student act on it? / 如果辅导系统把这个数值报告给学生，学生能据此做出调整吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**Notes (optional): how would you say this to a student? Anything unclear? / 备注（选填）：您会怎样对学生说这一点？有不清楚的地方吗？**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 20. Intonation error: sharp or flat / 音准偏差（偏高或偏低） · *incoming (v18) / 即将加入（v18）*
`pitch_dev_semi`

**How teachers say it / 老师的说法:**
- constant adjustment · quoted / 原文引用: Galamian, Principles of Violin Playing and Teaching (1962)
- Intonation · attributed to / 转述自: Fischer, Basics (1997), section F heading
- sharp / flat · measurement study / 实验研究: feedback wording in the experimental literature (Salzberg 1980)
- 音准 · quoted / 原文引用: 肖柯 (2016)；麻西水 (2002)，文章标题
- 准 · quoted / 原文引用: 林耀基 口诀，见 杨宝智《林耀基小提琴教学法精要》(2004)

**What it measures / 测量内容:** How far the pitch actually played is from the written pitch of the note. / 实际演奏的音高与乐谱上写的音高相差多少。  
**Unit / 单位:** semitones; 100 cents make one semitone / 半音；1 个半音 = 100 音分  
**Range / 取值范围:** 0 = exactly the written pitch; positive = sharp; negative = flat; 0.5 = a quarter-tone off / 0 = 与谱面一致；正值 = 偏高；负值 = 偏低；0.5 = 差四分之一音

**H1.** Is this something violin teachers actually attend to in lessons? / 小提琴老师在课上真的会关注这一点吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**H2.** If a tutor reported this value to a student, could the student act on it? / 如果辅导系统把这个数值报告给学生，学生能据此做出调整吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**Notes (optional): how would you say this to a student? Anything unclear? / 备注（选填）：您会怎样对学生说这一点？有不清楚的地方吗？**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 21. Loudness / 音量（响度）
`env_db`

**How teachers say it / 老师的说法:**
- dynamics (No dynamics, Simple Dynamics, Inter. dynamics) · expert spreadsheet / 专家表格: ViolinITS etude classification spreadsheet, "Tone" columns
- nuance · attributed to / 转述自: Auer, Violin Playing as I Teach It (1921), chapter topic
- volume / a bigger sound · paraphrase, uncited / 转述，未引用
- 音量 / 力度 · paraphrase, uncited / 转述，未引用

**What it measures / 测量内容:** How loud the sound is at each moment, as the ear would hear it rise and fall. / 每一时刻声音有多响，即听觉上音量的起伏。  
**Unit / 单位:** decibels, a log scale of sound level / 分贝，声音强度的对数刻度  
**Range / 取值范围:** higher = louder; very low = silence / 越高越响；很低 = 静音

**H1.** Is this something violin teachers actually attend to in lessons? / 小提琴老师在课上真的会关注这一点吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**H2.** If a tutor reported this value to a student, could the student act on it? / 如果辅导系统把这个数值报告给学生，学生能据此做出调整吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**Notes (optional): how would you say this to a student? Anything unclear? / 备注（选填）：您会怎样对学生说这一点？有不清楚的地方吗？**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 22. Note attack strength / 起音（发音）强度
`onset_strength`

**How teachers say it / 老师的说法:**
- articulation · measurement study / 实验研究: Cavitt (2003), teacher correction targets (band rehearsals)
- Accent / Sfz, Martelé & Marcato · expert spreadsheet / 专家表格: ViolinITS etude classification spreadsheet, "Bow strokes" columns
- key bow strokes · attributed to / 转述自: Fischer, Basics (1997), section C
- attack / the start of the note · paraphrase, uncited / 转述，未引用
- 发音 / 起音 / 音头 · paraphrase, uncited / 转述，未引用

**What it measures / 测量内容:** How strongly a new note is beginning at each moment: high at a clear, accented attack, low in the middle of a sustained note. / 每一时刻新音开始的强弱程度：清晰、有重音的起音时高，持续音中间时低。  
**Unit / 单位:** an attack-strength score with no physical unit / 起音强度分值，没有物理单位  
**Range / 取值范围:** 0 = no new note starting; larger = a stronger, sharper attack / 0 = 没有新音开始；越大 = 起音越强、越突出

**H1.** Is this something violin teachers actually attend to in lessons? / 小提琴老师在课上真的会关注这一点吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**H2.** If a tutor reported this value to a student, could the student act on it? / 如果辅导系统把这个数值报告给学生，学生能据此做出调整吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**Notes (optional): how would you say this to a student? Anything unclear? / 备注（选填）：您会怎样对学生说这一点？有不清楚的地方吗？**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 23. Pitch being played / 正在演奏的音高
`f0_midi`

**How teachers say it / 老师的说法:**
- constant adjustment · quoted / 原文引用: Galamian, Principles of Violin Playing and Teaching (1962)
- flat 3rd finger · attributed to / 转述自: Hamann & Gillespie, Strategies for Teaching Strings (4th ed., 2018)
- 准 · quoted / 原文引用: 林耀基 口诀，见 杨宝智《林耀基小提琴教学法精要》(2004)
- 音准 · quoted / 原文引用: 肖柯 (2016)；麻西水 (2002)，文章标题
- the note you are playing · paraphrase, uncited / 转述，未引用

**What it measures / 测量内容:** The pitch the violin is sounding at each moment, tracked continuously, so vibrato, slides and out-of-tune notes all show. / 每一时刻小提琴发出的音高，连续跟踪，因此揉弦、滑音和音不准都会体现出来。  
**Unit / 单位:** piano-key numbers with fractions; a step of 1 is one semitone / 钢琴键号（带小数）；每 1 为一个半音  
**Range / 取值范围:** higher = higher pitch, over the violin's range from the open G string upward / 越高音越高，覆盖从空弦 G 起的小提琴音域

**H1.** Is this something violin teachers actually attend to in lessons? / 小提琴老师在课上真的会关注这一点吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**H2.** If a tutor reported this value to a student, could the student act on it? / 如果辅导系统把这个数值报告给学生，学生能据此做出调整吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**Notes (optional): how would you say this to a student? Anything unclear? / 备注（选填）：您会怎样对学生说这一点？有不清楚的地方吗？**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 24. Pitch clarity: how clearly a pitch is present / 音高清晰度（声音里有多明确的音高）
`f0_salience`

**How teachers say it / 老师的说法:**
- It is impossible to scratch if the bow keeps moving · quoted / 原文引用: Fischer, The Violin Lesson (2013), chapter heading
- scratchy tone · attributed to / 转述自: Hamann & Gillespie, Strategies for Teaching Strings (4th ed., 2018)
- tonalization · quoted / 原文引用: Suzuki, as described in Starr, The Suzuki Violinist
- 匀、美 · quoted / 原文引用: 林耀基 口诀，见 杨宝智《林耀基小提琴教学法精要》(2004)
- clean, focused tone · paraphrase, uncited / 转述，未引用
- 声音干净 / 有核心 · paraphrase, uncited / 转述，未引用

**What it measures / 测量内容:** How clearly a definite pitch is present in the sound at each moment: high for a clean, focused tone, low for scratch, noise or silence. / 每一时刻声音里有多明确的音高：声音干净、有核心时高，刮擦、噪音或静音时低。  
**Unit / 单位:** a pitch-evidence score with no physical unit / 音高证据分值，没有物理单位  
**Range / 取值范围:** near 0 = no clear pitch (silence or noise); larger = a clearer, more focused pitch / 接近 0 = 没有明确音高（静音或噪音）；越大 = 音高越清晰、越集中

**H1.** Is this something violin teachers actually attend to in lessons? / 小提琴老师在课上真的会关注这一点吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**H2.** If a tutor reported this value to a student, could the student act on it? / 如果辅导系统把这个数值报告给学生，学生能据此做出调整吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**Notes (optional): how would you say this to a student? Anything unclear? / 备注（选填）：您会怎样对学生说这一点？有不清楚的地方吗？**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 25. Played on a different string than the score implies / 所用琴弦与乐谱暗示的不同
`string_disagreement`

**How teachers say it / 老师的说法:**
- wrong string / play it on the A string · paraphrase, uncited / 转述，未引用
- String/s · expert spreadsheet / 专家表格: ViolinITS etude classification spreadsheet, metadata column
- building stepwise fingers on one string (D) · expert spreadsheet / 专家表格: ViolinITS etude classification spreadsheet, goal text
- 弦用错了 / 在 A 弦上拉 · paraphrase, uncited / 转述，未引用

**What it measures / 测量内容:** How strongly the evidence from the sound and the left hand says the note was played on a different string from the one the written music implies. / 根据声音和左手的证据，这个音在与乐谱暗示不同的琴弦上演奏的可能性有多大。  
**Unit / 单位:** a score from 0 to 1 / 0 到 1 之间的分值  
**Range / 取值范围:** 0 = the same string as the score implies; 1 = clearly a different string; blank when the score gives no usable string / 0 = 与乐谱暗示的弦相同；1 = 明确是另一根弦；乐谱无法判定时为空

**H1.** Is this something violin teachers actually attend to in lessons? / 小提琴老师在课上真的会关注这一点吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**H2.** If a tutor reported this value to a student, could the student act on it? / 如果辅导系统把这个数值报告给学生，学生能据此做出调整吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**Notes (optional): how would you say this to a student? Anything unclear? / 备注（选填）：您会怎样对学生说这一点？有不清楚的地方吗？**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 26. Left-hand position, compared with what the score implies / 左手把位（与乐谱暗示的把位相比）
`position_dev_semi`

**How teachers say it / 老师的说法:**
- position changing · attributed to / 转述自: Fischer, The Violin Lesson (2013), lesson topic; Fischer, Basics (1997), section E "Shifting"
- Position, Small Shifting · expert spreadsheet / 专家表格: ViolinITS etude classification spreadsheet, "Hand Frame" columns
- missed shift · attributed to / 转述自: Gerle, The Art of Practising the Violin (1983)
- 换把 / 手型 · quoted / 原文引用: 丁芷诺《小提琴基本功强化训练教材》（上海音乐出版社）
- stay in third position · paraphrase, uncited / 转述，未引用

**What it measures / 测量内容:** Where on the fingerboard the left hand actually was for the note, compared with the position the written music implies. / 演奏这个音时左手实际所在的把位，与乐谱暗示的把位相比较。  
**Unit / 单位:** semitones along the string / 沿弦的半音数  
**Range / 取值范围:** 0 = the position the score implies; positive = higher up the fingerboard than implied; negative = lower / 0 = 乐谱暗示的把位；正值 = 比暗示的更靠上（高把位）；负值 = 更靠下

**H1.** Is this something violin teachers actually attend to in lessons? / 小提琴老师在课上真的会关注这一点吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**H2.** If a tutor reported this value to a student, could the student act on it? / 如果辅导系统把这个数值报告给学生，学生能据此做出调整吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**Notes (optional): how would you say this to a student? Anything unclear? / 备注（选填）：您会怎样对学生说这一点？有不清楚的地方吗？**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 27. The player's habitual sounding point / 演奏者惯常的触弦点
`contact_bridge_ratio_neutral`

**How teachers say it / 老师的说法:**
- soundpoint / the five soundpoints · attributed to / 转述自: Fischer, The Violin Lesson (2013)
- contact point · attributed to / 转述自: Flesch, The Art of Violin Playing, Book 1
- the bow drifting from the contact point · attributed to / 转述自: Starr, The Suzuki Violinist
- 匀 · quoted / 原文引用: 林耀基 口诀，见 杨宝智《林耀基小提琴教学法精要》(2004)
- playing too close to the fingerboard / too close to the bridge · paraphrase, uncited / 转述，未引用
- 触弦点 · paraphrase, uncited / 转述，未引用

**What it measures / 测量内容:** The player's usual contact point in that recording: where along the string the bow hair most often sits, between the bridge and the fingerboard. / 演奏者在这次录音中惯常的触弦点：弓毛在琴马与指板之间最常处的位置。  
**Unit / 单位:** a fraction of the string length (bridge to nut) / 弦长（琴马到琴枕）的比例  
**Range / 取值范围:** 0 = at the bridge; larger = further toward the fingerboard; one value per recording, not per moment / 0 = 在琴马处；越大 = 越靠近指板；每段录音一个值，而不是每一时刻

**H1.** Is this something violin teachers actually attend to in lessons? / 小提琴老师在课上真的会关注这一点吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**H2.** If a tutor reported this value to a student, could the student act on it? / 如果辅导系统把这个数值报告给学生，学生能据此做出调整吗？  
☐ 1 clearly no 明显不是 · ☐ 2 probably no 可能不是 · ☐ 3 probably yes 可能是 · ☐ 4 clearly yes 明显是

**Notes (optional): how would you say this to a student? Anything unclear? / 备注（选填）：您会怎样对学生说这一点？有不清楚的地方吗？**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

