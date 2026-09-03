# Violin teaching survey · round 0

**form version:** `4673b2d432b2` · **rater:** ☐ the violinist · ☐ the author (Siyuan)

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

**Teachers might say:** “bow speed” (Fischer; Flesch) · “It is impossible to scratch if the bow keeps moving” (Fischer) · “evenness, accuracy, beauty” (Lin Yaoji)

**What this is:** How fast the bow is moving, and whether it is going down-bow or up-bow.  
**Measured as:** bow-lengths per second (1 = a full bow in one second)  
**What the numbers mean:** 0 = the bow is not moving; above 0 = down-bow; below 0 = up-bow

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 2. Bow-hand wrist turn, direction 3 of 3, compared with the player's usual
<sub>right_wrist_aa_z_dev_deg</sub>  
**Warm-up card: answer it like any other.**

**Teachers might say:** “bent wrist” (Rolland) · “wrist flexion at the frog” (a teaching syllabus)

**What this is:** One of three ways the bow-hand wrist can turn, as a computer body model measures it, compared with this player's usual wrist position. The three directions belong to the model; they are not the words a teacher would use, such as "bent" or "flexed".  
**Measured as:** degrees (an estimate from a body model, not a medical measurement)  
**What the numbers mean:** 0 = the player's usual wrist position; above or below 0 = turned one way or the other

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 3. Where the bow touches the string, compared with the player's usual spot
<sub>contact_bridge_ratio_dev</sub>

**Teachers might say:** “soundpoint” (Fischer) · “contact point” (Flesch) · “the bow drifting from the contact point” (Starr (Suzuki method)) · “evenness” (Lin Yaoji)

**What this is:** Whether the bow is touching the string closer to the bridge or closer to the fingerboard than this player usually does.  
**Measured as:** a share of the string's length  
**What the numbers mean:** 0 = the player's usual spot; below 0 = closer to the bridge than usual; above 0 = closer to the fingerboard than usual

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 4. Which part of the bow is on the string
<sub>hair_pos</sub>

**Teachers might say:** “at the frog / in the middle / at the tip” (common saying) · “bow distribution” (a teaching syllabus) · “whole bows” (Fischer)

**What this is:** Whether the player is using the bow near the frog (the hand end), the middle, or the tip.  
**Measured as:** a share of the bow's length  
**What the numbers mean:** 0 = at the frog; 0.5 = the middle of the bow; 1 = at the tip

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 5. Is the bow on the string or lifted off?
<sub>hair_string_gap_ratio</sub>

**Teachers might say:** “bow on the string / off the string” (common saying) · “spiccato, sautillé, ricochet (off-the-string strokes)” (a teaching syllabus)

**What this is:** How far the bow hair is from the string: zero when the bow is on the string, more when it is lifted off.  
**Measured as:** a share of the string's length  
**What the numbers mean:** 0 = on the string; bigger = lifted further off

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 6. Is the bow straight or crooked?
<sub>skew_deg</sub>

**Teachers might say:** “crooked bow” (Hamann & Gillespie) · “keep the bow straight” (common saying) · “bow–string angle” (a research study)

**What this is:** How far the bow is from being at a right angle to the strings, in other words how crooked the bow stroke is.  
**Measured as:** degrees  
**What the numbers mean:** 0 = perfectly straight; bigger = more crooked, in either direction

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 7. Which string the bow is leaning toward
<sub>string_side_deg</sub>

**Teachers might say:** “string crossing” (Galamian; Rolland) · “bow tilt” (a research study) · “string level” (common saying)

**What this is:** The tilt of the bow around the strings, which shows which string it is playing on or moving toward.  
**Measured as:** degrees  
**What the numbers mean:** smaller = toward the G string (the lowest); larger = toward the E string (the highest)

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 8. Bow speed, including direction
<sub>bow_speed</sub>

**Teachers might say:** “bow speed” (Fischer; Flesch) · “It is impossible to scratch if the bow keeps moving” (Fischer) · “evenness, accuracy, beauty” (Lin Yaoji)

**What this is:** How fast the bow is moving, and whether it is going down-bow or up-bow.  
**Measured as:** bow-lengths per second (1 = a full bow in one second)  
**What the numbers mean:** 0 = the bow is not moving; above 0 = down-bow; below 0 = up-bow

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 9. Bow speed, ignoring direction
<sub>bow_speed_abs</sub>

**Teachers might say:** “bow speed” (Fischer; Flesch) · “the bow keeps moving” (Fischer)

**What this is:** How fast the bow is moving, whether it is a down-bow or an up-bow.  
**Measured as:** bow-lengths per second (1 = a full bow in one second)  
**What the numbers mean:** 0 = not moving; bigger = faster

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 10. How quickly the bow speeds up or slows down
<sub>bow_accel</sub>

**Teachers might say:** “speeding up or slowing down the bow within a stroke” (common saying) · “martelé, marcato, accents” (a teaching syllabus)

**What this is:** Whether the bow is speeding up, slowing down, or moving at a steady speed during a stroke.  
**Measured as:** change in bow speed per second  
**What the numbers mean:** 0 = steady speed; bigger = the speed is changing more quickly

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 11. Down-bow or up-bow
<sub>direction_sign</sub>

**Teachers might say:** “down-bow / up-bow” (common saying)

**What this is:** Whether the bow is moving as a down-bow or an up-bow, passing smoothly through zero when it turns around.  
**Measured as:** a value between −1 and +1  
**What the numbers mean:** +1 = clearly down-bow; −1 = clearly up-bow; near 0 = stopped or changing direction

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 12. How bent the bow-arm elbow is
<sub>right_elbow_flexion_deg</sub>

**Teachers might say:** “elbow angle / elbow height of the bow arm” (common saying) · “whole-arm strokes” (Rolland; Galamian) · “changing notes without changing the arm shape” (Lin Yaoji)

**What this is:** How much the right elbow is bent, estimated from a computer model of the player's body.  
**Measured as:** degrees (an estimate from a body model, not a medical measurement)  
**What the numbers mean:** 0 = arm straight; bigger = more bent

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 13. Bow-hand wrist turn, direction 1 of 3, compared with the player's usual
<sub>right_wrist_aa_x_dev_deg</sub>

**Teachers might say:** “bent wrist” (Rolland) · “wrist flexion at the frog” (a teaching syllabus)

**What this is:** One of three ways the bow-hand wrist can turn, as a computer body model measures it, compared with this player's usual wrist position. The three directions belong to the model; they are not the words a teacher would use, such as "bent" or "flexed".  
**Measured as:** degrees (an estimate from a body model, not a medical measurement)  
**What the numbers mean:** 0 = the player's usual wrist position; above or below 0 = turned one way or the other

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 14. Bow-hand wrist turn, direction 2 of 3, compared with the player's usual
<sub>right_wrist_aa_y_dev_deg</sub>

**Teachers might say:** “bent wrist” (Rolland) · “wrist flexion at the frog” (a teaching syllabus)

**What this is:** One of three ways the bow-hand wrist can turn, as a computer body model measures it, compared with this player's usual wrist position. The three directions belong to the model; they are not the words a teacher would use, such as "bent" or "flexed".  
**Measured as:** degrees (an estimate from a body model, not a medical measurement)  
**What the numbers mean:** 0 = the player's usual wrist position; above or below 0 = turned one way or the other

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 15. Bow-hand wrist turn, direction 3 of 3, compared with the player's usual
<sub>right_wrist_aa_z_dev_deg</sub>

**Teachers might say:** “bent wrist” (Rolland) · “wrist flexion at the frog” (a teaching syllabus)

**What this is:** One of three ways the bow-hand wrist can turn, as a computer body model measures it, compared with this player's usual wrist position. The three directions belong to the model; they are not the words a teacher would use, such as "bent" or "flexed".  
**Measured as:** degrees (an estimate from a body model, not a medical measurement)  
**What the numbers mean:** 0 = the player's usual wrist position; above or below 0 = turned one way or the other

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 16. Bow-arm shoulder position, compared with the player's usual
<sub>right_shoulder_rotation_dev_deg</sub>

**Teachers might say:** “raised shoulder” (Rolland) · “gripping / clamping” (Havas) · “let the violin become part of the body” (Lin Yaoji)

**What this is:** How much the right shoulder has moved away from this player's usual shoulder position, for example raised or hunched.  
**Measured as:** degrees (an estimate from a body model, not a medical measurement)  
**What the numbers mean:** 0 = the usual position; bigger = further from it

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 17. Head tilt
<sub>neck_tilt_deg</sub>

**Teachers might say:** “head position / head tilt” (common saying) · “chin or jaw pressure” (a teaching syllabus)

**What this is:** How far the head and neck are tilted away from upright, in any direction.  
**Measured as:** degrees (an estimate from a body model)  
**What the numbers mean:** 0 = upright; bigger = more tilted

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 18. Posture: upright or slouched
<sub>spine_curvature_deg</sub>

**Teachers might say:** “posture” (Kreitman; Flesch) · “balanced stance” (Rolland) · “slouching” (common saying)

**What this is:** How much the upper body is bent forward or sideways from upright.  
**Measured as:** degrees (an estimate from a body model)  
**What the numbers mean:** 0 = upright; bigger = more bent

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 19. How high the violin is held
<sub>violin_hold_height_ratio</sub>

**Teachers might say:** “scroll drooping” (Auer) · “violin drifting over the right arm” (Starr (Suzuki method)) · “instrument support” (Rolland) · “let the violin become part of the body” (Lin Yaoji)

**What this is:** How high the violin sits compared with the player's hips: lower when the scroll droops, higher when the violin is held up.  
**Measured as:** a share of the string's length (so body size does not matter)  
**What the numbers mean:** bigger = the violin is held higher

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 20. In tune, sharp, or flat
<sub>pitch_dev_semi</sub>

**Teachers might say:** “constant adjustment” (Galamian) · “Intonation” (Fischer) · “sharp / flat” (a research study) · “intonation” (Chinese teaching articles) · “accuracy” (Lin Yaoji)

**What this is:** How far the note played is from the note written in the music.  
**Measured as:** semitones (the distance between two neighbouring piano keys; 100 cents)  
**What the numbers mean:** 0 = in tune; above 0 = sharp; below 0 = flat; 0.5 = a quarter-tone off

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 21. Loudness
<sub>env_db</sub>

**Teachers might say:** “dynamics” (a teaching syllabus) · “nuance” (Auer) · “volume / a bigger sound” (common saying)

**What this is:** How loud the sound is from moment to moment.  
**Measured as:** decibels  
**What the numbers mean:** higher = louder; very low = silence

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 22. How strongly each note starts
<sub>onset_strength</sub>

**Teachers might say:** “articulation” (a research study) · “accents, martelé, marcato” (a teaching syllabus) · “key bow strokes” (Fischer) · “attack / the start of the note” (common saying)

**What this is:** How clearly and strongly a new note begins: high for a crisp, accented start, low in the middle of a held note.  
**Measured as:** a score with no unit  
**What the numbers mean:** 0 = no note starting; bigger = a stronger start

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 23. The note being played
<sub>f0_midi</sub>

**Teachers might say:** “constant adjustment” (Galamian) · “flat 3rd finger” (Hamann & Gillespie) · “accuracy” (Lin Yaoji) · “intonation” (Chinese teaching articles) · “the note you are playing” (common saying)

**What this is:** Which pitch the violin is sounding at each moment, tracked continuously, so vibrato, slides and tuning all show.  
**Measured as:** piano-key numbers, with fractions in between  
**What the numbers mean:** higher = a higher note

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 24. How clean and clear the tone is
<sub>f0_salience</sub>

**Teachers might say:** “It is impossible to scratch if the bow keeps moving” (Fischer) · “scratchy tone” (Hamann & Gillespie) · “tonalization” (Suzuki) · “evenness, beauty” (Lin Yaoji) · “clean, focused tone” (common saying)

**What this is:** How clearly a definite note can be heard in the sound: high for a clean, focused tone, low for scratchy, noisy or silent moments.  
**Measured as:** a score with no unit  
**What the numbers mean:** near 0 = no clear note (silence or noise); bigger = a clearer tone

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 25. Played on a different string than the music suggests
<sub>string_disagreement</sub>

**Teachers might say:** “wrong string / play it on the A string” (common saying) · “which string(s) a piece uses” (a teaching syllabus) · “building stepwise fingers on one string (D)” (a teaching syllabus)

**What this is:** How likely it is that the player used a different string from the one the written music points to.  
**Measured as:** a score from 0 to 1  
**What the numbers mean:** 0 = the same string the music suggests; 1 = clearly a different string; blank when the music does not say

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 26. Left-hand position, compared with what the music suggests
<sub>position_dev_semi</sub>

**Teachers might say:** “position changing” (Fischer) · “position, small shifts” (a teaching syllabus) · “missed shift” (Gerle) · “shifting / hand frame” (Ding Zhinuo) · “stay in third position” (common saying)

**What this is:** Whether the left hand was higher or lower on the fingerboard than the position the written music points to.  
**Measured as:** semitones along the string  
**What the numbers mean:** 0 = the expected position; above 0 = higher up the fingerboard; below 0 = lower

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 27. The player's usual bow-contact spot
<sub>contact_bridge_ratio_neutral</sub>

**Teachers might say:** “soundpoint” (Fischer) · “contact point” (Flesch) · “the bow drifting from the contact point” (Starr (Suzuki method)) · “evenness” (Lin Yaoji) · “playing too close to the fingerboard / too close to the bridge” (common saying)

**What this is:** Where on the string this player's bow usually sits during a recording, between the bridge and the fingerboard.  
**Measured as:** a share of the string's length  
**What the numbers mean:** 0 = at the bridge; bigger = closer to the fingerboard; one number for the whole recording

**Question 1.** Do violin teachers pay attention to this in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app told a student this number, could the student do something useful with it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

