# Violin teaching survey · round 0

**form version:** `880a346ff874` · **rater:** ☐ the violinist · ☐ the author (Siyuan)

Paper version: cards in a fixed order, tick one box per question.

We built a computer system that watches and listens to someone playing the violin and measures 27 different things. Each card below describes one of them in plain words. For each one, tell us two things: do violin teachers care about it, and could a student use the number? There are no right answers.

## The two questions

**Question 1.** Do violin teachers pay attention to this in lessons?

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
*We mean the number itself. "Your bow speed changed a lot in this phrase" is something a student can work on; a number with no obvious lesson behind it is not.*

## How to answer

- **1** definitely not
- **2** probably not
- **3** probably yes
- **4** definitely yes

---

### 1. Bow speed, including direction
<sub>bow_speed</sub>  
**Warm-up card: answer it like any other.**

This measures how fast the bow is moving and whether it is a down-bow or an up-bow. It is counted in bow-lengths per second, so 1 means a full bow in one second; zero means the bow is not moving, above zero is a down-bow, and below zero is an up-bow. Teachers usually just call this "bow speed" (Fischer; Flesch); Fischer adds that "it is impossible to scratch if the bow keeps moving", and Lin Yaoji's maxim "evenness, accuracy, beauty" begins with an even bow.

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 2. Bow-hand wrist turn, direction 3 of 3, compared with the player's usual
<sub>right_wrist_aa_z_dev_deg</sub>  
**Warm-up card: answer it like any other.**

This is one of three ways the bow-hand wrist can turn, as a computer body model measures it, compared with this player's usual wrist position. It is given in degrees: zero is the player's usual position, and numbers above or below zero mean the wrist is turned one way or the other. The three directions belong to the model, not to a teacher's vocabulary; the nearest teacher phrases are a "bent wrist" (Rolland) and "wrist flexion at the frog" (a teaching syllabus).

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 3. Where the bow touches the string, compared with the player's usual spot
<sub>contact_bridge_ratio_dev</sub>

This measures where the bow touches the string, compared with the spot this player usually uses. It is a share of the string's length between the bridge and the fingerboard, so zero means the player's usual spot, a negative number means closer to the bridge than usual, and a positive number means closer to the fingerboard than usual. Teachers call this spot the "soundpoint" (Fischer) or the "contact point" (Flesch) and warn about "the bow drifting from the contact point" (Starr); Lin Yaoji's maxim of "evenness" is about keeping it steady.

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 4. Which part of the bow is on the string
<sub>hair_pos</sub>

This measures which part of the bow is on the string: near the frog (the hand end), the middle, or the tip. It is a share of the bow's length, so 0 means the frog, 0.5 the middle and 1 the tip. Teachers talk about playing "at the frog", "in the middle" or "at the tip", about "bow distribution" (a teaching syllabus), and about using "whole bows" (Fischer).

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 5. Is the bow on the string or lifted off?
<sub>hair_string_gap_ratio</sub>

This measures how far the bow hair is from the string. It is zero when the bow is on the string and grows as the bow is lifted off, counted as a share of the string's length. Teachers speak of the bow being "on the string" or "off the string", and of off-the-string strokes such as spiccato, sautillé and ricochet (a teaching syllabus).

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 6. Is the bow straight or crooked?
<sub>skew_deg</sub>

This measures how far the bow is from being at a right angle to the strings, in other words how crooked the bow stroke is. It is given in degrees: zero is a perfectly straight bow, and bigger numbers mean more crooked, in either direction. Teachers say "keep the bow straight" and diagnose a "crooked bow" (Hamann & Gillespie); a research study calls it the "bow–string angle".

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 7. Which string the bow is leaning toward
<sub>string_side_deg</sub>

This measures the tilt of the bow around the strings, which shows which string the bow is playing on or moving toward. It is an angle in degrees: smaller numbers lean toward the G string, the lowest, and larger numbers toward the E string, the highest. Teachers talk about "string crossing" (Galamian; Rolland) and "string level"; a research study calls it "bow tilt".

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 8. Bow speed, including direction
<sub>bow_speed</sub>

This measures how fast the bow is moving and whether it is a down-bow or an up-bow. It is counted in bow-lengths per second, so 1 means a full bow in one second; zero means the bow is not moving, above zero is a down-bow, and below zero is an up-bow. Teachers usually just call this "bow speed" (Fischer; Flesch); Fischer adds that "it is impossible to scratch if the bow keeps moving", and Lin Yaoji's maxim "evenness, accuracy, beauty" begins with an even bow.

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 9. Bow speed, ignoring direction
<sub>bow_speed_abs</sub>

This measures how fast the bow is moving, ignoring whether it is a down-bow or an up-bow. It is counted in bow-lengths per second: zero means not moving, 1 means a full bow in one second, and bigger numbers mean faster. Teachers call this "bow speed" (Fischer; Flesch) and remind students to keep "the bow moving" (Fischer).

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 10. How quickly the bow speeds up or slows down
<sub>bow_accel</sub>

This measures whether the bow is speeding up, slowing down, or moving at a steady speed during a stroke. It is the change in bow speed per second: zero means a steady speed, and bigger numbers mean the speed is changing more quickly. Teachers describe "speeding up or slowing down the bow within a stroke" and teach accented strokes such as martelé and marcato (a teaching syllabus).

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 11. Down-bow or up-bow
<sub>direction_sign</sub>

This tells whether the bow is moving as a down-bow or an up-bow. It runs from −1 to +1: +1 is clearly a down-bow, −1 is clearly an up-bow, and values near zero mean the bow is stopped or changing direction. Teachers simply say "down-bow" and "up-bow".

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 12. How bent the bow-arm elbow is
<sub>right_elbow_flexion_deg</sub>

This measures how much the right elbow, the bow-arm elbow, is bent, estimated from a computer model of the player's body rather than a medical measurement. It is given in degrees: zero is a straight arm, and bigger numbers mean more bend. Teachers talk about the "elbow angle" or "elbow height" of the bow arm and about "whole-arm strokes" (Rolland; Galamian); Lin Yaoji speaks of "changing notes without changing the arm shape".

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 13. Bow-hand wrist turn, direction 1 of 3, compared with the player's usual
<sub>right_wrist_aa_x_dev_deg</sub>

This is one of three ways the bow-hand wrist can turn, as a computer body model measures it, compared with this player's usual wrist position. It is given in degrees: zero is the player's usual position, and numbers above or below zero mean the wrist is turned one way or the other. The three directions belong to the model, not to a teacher's vocabulary; the nearest teacher phrases are a "bent wrist" (Rolland) and "wrist flexion at the frog" (a teaching syllabus).

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 14. Bow-hand wrist turn, direction 2 of 3, compared with the player's usual
<sub>right_wrist_aa_y_dev_deg</sub>

This is one of three ways the bow-hand wrist can turn, as a computer body model measures it, compared with this player's usual wrist position. It is given in degrees: zero is the player's usual position, and numbers above or below zero mean the wrist is turned one way or the other. The three directions belong to the model, not to a teacher's vocabulary; the nearest teacher phrases are a "bent wrist" (Rolland) and "wrist flexion at the frog" (a teaching syllabus).

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 15. Bow-hand wrist turn, direction 3 of 3, compared with the player's usual
<sub>right_wrist_aa_z_dev_deg</sub>

This is one of three ways the bow-hand wrist can turn, as a computer body model measures it, compared with this player's usual wrist position. It is given in degrees: zero is the player's usual position, and numbers above or below zero mean the wrist is turned one way or the other. The three directions belong to the model, not to a teacher's vocabulary; the nearest teacher phrases are a "bent wrist" (Rolland) and "wrist flexion at the frog" (a teaching syllabus).

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 16. Bow-arm shoulder position, compared with the player's usual
<sub>right_shoulder_rotation_dev_deg</sub>

This measures how much the right shoulder, the bow-arm shoulder, has moved away from this player's usual shoulder position, for example when it is raised or hunched. It is given in degrees from a computer body model: zero is the usual position, and bigger numbers mean further from it. Teachers warn about a "raised shoulder" (Rolland) and about "gripping" or "clamping" (Havas), and Lin Yaoji says to "let the violin become part of the body".

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 17. Head tilt
<sub>neck_tilt_deg</sub>

This measures how far the head and neck are tilted away from upright, in any direction, estimated from a computer body model. It is given in degrees: zero is upright, and bigger numbers mean more tilt. Teachers talk about "head position" or "head tilt" and about "chin or jaw pressure" (a teaching syllabus).

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 18. Posture: upright or slouched
<sub>spine_curvature_deg</sub>

This measures how much the upper body is bent forward or sideways from upright, estimated from a computer body model. It is given in degrees: zero is upright, and bigger numbers mean more bend. Teachers simply call this "posture" (Kreitman; Flesch) or a "balanced stance" (Rolland), and when it goes wrong, "slouching".

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 19. How high the violin is held
<sub>violin_hold_height_ratio</sub>

This measures how high the violin sits compared with the player's hips: lower when the scroll droops, higher when the violin is held up. It is a share of the string's length, so body size does not matter, and bigger numbers mean the violin is held higher. Teachers warn about "scroll drooping" (Auer) and the "violin drifting over the right arm" (Starr), talk about "instrument support" (Rolland), and in Lin Yaoji's words aim to "let the violin become part of the body".

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 20. In tune, sharp, or flat
<sub>pitch_dev_semi</sub>

This measures how far the note played is from the note written in the music. It is given in semitones, the distance between two neighbouring piano keys or 100 cents: zero is in tune, above zero is sharp, below zero is flat, and 0.5 is a quarter-tone off. Teachers call this "intonation" (Fischer) and say a note is "sharp" or "flat"; Galamian describes tuning as "constant adjustment", and Lin Yaoji's maxim asks for "accuracy".

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 21. Loudness
<sub>env_db</sub>

This measures how loud the sound is from moment to moment. It is given in decibels: higher numbers are louder, and very low numbers mean silence. Teachers talk about "dynamics" (a teaching syllabus), "nuance" (Auer), and "volume" or "a bigger sound".

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 22. How strongly each note starts
<sub>onset_strength</sub>

This measures how clearly and strongly each new note begins: high for a crisp, accented start and low in the middle of a held note. It is a score with no unit: zero means no note is starting, and bigger numbers mean a stronger start. Teachers talk about the "attack" or "the start of the note", about "articulation" (a research study), and about accented strokes such as martelé and marcato and the "key bow strokes" (Fischer).

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 23. The note being played
<sub>f0_midi</sub>

This measures which pitch the violin is sounding at each moment, tracked continuously, so vibrato, slides and tuning all show. It is given as piano-key numbers with fractions in between: higher numbers are higher notes. Teachers simply talk about "the note you are playing"; Galamian calls tuning it "constant adjustment", Hamann & Gillespie mention a "flat 3rd finger", and Lin Yaoji's maxim asks for "accuracy".

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 24. How clean and clear the tone is
<sub>f0_salience</sub>

This measures how clearly a definite note can be heard in the sound: high for a clean, focused tone and low for scratchy, noisy or silent moments. It is a score with no unit: near zero means no clear note, and bigger numbers mean a clearer tone. Teachers talk about a "clean, focused tone" and a "scratchy tone" (Hamann & Gillespie); Fischer says "it is impossible to scratch if the bow keeps moving", Suzuki teachers practise "tonalization", and Lin Yaoji's maxim asks for "evenness" and "beauty".

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 25. Played on a different string than the music suggests
<sub>string_disagreement</sub>

This measures how likely it is that the player used a different string from the one the written music points to. It is a score from 0 to 1: zero means the same string the music suggests, 1 means clearly a different string, and it is left blank when the music does not say. Teachers say things like "wrong string" or "play it on the A string", and teaching materials note which string or strings a piece uses (a teaching syllabus).

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 26. Left-hand position, compared with what the music suggests
<sub>position_dev_semi</sub>

This measures whether the left hand was higher or lower on the fingerboard than the position the written music points to. It is given in semitones along the string: zero is the expected position, above zero is higher up the fingerboard, and below zero is lower. Teachers say "stay in third position", teach "position changing" (Fischer), "shifting" and the "hand frame" (Ding Zhinuo), and diagnose a "missed shift" (Gerle).

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 27. The player's usual bow-contact spot
<sub>contact_bridge_ratio_neutral</sub>

This is where on the string this player's bow usually sits during a recording, between the bridge and the fingerboard, as one number for the whole recording. It is a share of the string's length: zero is at the bridge, and bigger numbers are closer to the fingerboard. Teachers call this spot the "soundpoint" (Fischer) or "contact point" (Flesch) and warn about "playing too close to the fingerboard" or "too close to the bridge"; Lin Yaoji's maxim of "evenness" is about keeping it steady.

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

