# Violin teaching survey · round 0

**form version:** `d7e500d220d3` · **rater:** ☐ the violinist · ☐ the author (Siyuan)

Paper version: cards in a fixed order, tick one box per question.

We built a computer program that watches and listens to someone playing the violin and keeps track of 27 different things. Each card describes one of them in everyday words. For each one, tell us two things: do violin teachers care about it, and could a student use the number? There are no right or wrong answers.

## The two questions

**Question 1.** Do violin teachers pay attention to this in lessons?

**Question 2.** If a practice app gave a student a number for this, could the student act on it?  
*We mean the number itself. Could a student practise differently because of it?*

## How to answer

- **1** definitely not
- **2** probably not
- **3** probably yes
- **4** definitely yes

---

### 1. Bow speed (with direction)
<sub>bow_speed</sub>  
**Warm-up card: answer it like any other.**

This records how fast the bow is moving, and whether it is a down-bow or an up-bow. The number is zero when the bow is still, above zero for a down-bow and below zero for an up-bow; the bigger the number, the faster the bow. Teachers call this "bow speed".

**Question 1.** Do violin teachers pay attention to bow speed in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app gave a student a number for bow speed, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 2. Bow-hand wrist turn, direction 3 of 3
<sub>right_wrist_aa_z_dev_deg</sub>  
**Warm-up card: answer it like any other.**

Our system watches the wrist of the bow hand and records how it is turned. It splits that turn into three directions, a bit like bending the wrist up and down, tilting it from side to side, and twisting it, though we cannot say exactly which direction is which. This card is about direction 3 of the three. The number is zero when the wrist is in the player's usual position, and it goes up or down as the wrist turns away from that. Teachers do not have a word for this; the closest is a "bent wrist".

**Question 1.** Do violin teachers pay attention to how the bow-hand wrist is turned in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app gave a student a number for how the bow-hand wrist is turned, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 3. Where the bow touches the string, compared with the player's usual spot
<sub>contact_bridge_ratio_dev</sub>

This records where the bow touches the string and compares it with the spot this player normally uses. The number is zero at the usual spot, below zero when the bow is nearer the bridge than usual, and above zero when it is nearer the fingerboard. Teachers call this spot the "sounding point" or "contact point".

**Question 1.** Do violin teachers pay attention to where the bow touches the string in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app gave a student a number for where the bow touches the string, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 4. Which part of the bow is on the string
<sub>hair_pos</sub>

This records which part of the bow is on the string: near the hand end (the frog), the middle, or the tip. The number is 0 at the frog, 0.5 in the middle and 1 at the tip. Teachers talk about playing "at the frog" or "at the tip".

**Question 1.** Do violin teachers pay attention to which part of the bow is on the string in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app gave a student a number for which part of the bow is on the string, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 5. Is the bow on the string or lifted off?
<sub>hair_string_gap_ratio</sub>

This records whether the bow is touching the string or lifted off it. The number is zero when the bow is on the string and grows as the bow lifts higher. Teachers speak of playing "on the string" or "off the string".

**Question 1.** Do violin teachers pay attention to whether the bow is on the string or lifted off in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app gave a student a number for whether the bow is on the string or lifted off, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 6. Is the bow straight or crooked?
<sub>skew_deg</sub>

This records whether the bow is straight or crooked, in other words whether it crosses the strings at a right angle. The number is zero for a perfectly straight bow and grows as the bow gets more crooked. Teachers say "keep the bow straight" or "your bow is crooked".

**Question 1.** Do violin teachers pay attention to how straight the bow is in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app gave a student a number for how straight the bow is, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 7. Which string the bow is leaning toward
<sub>string_side_deg</sub>

This records which string the bow is leaning toward. Lower numbers mean the bow is leaning toward the G string, the lowest one; higher numbers mean toward the E string, the highest one. Teachers talk about "string crossing".

**Question 1.** Do violin teachers pay attention to which string the bow is leaning toward in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app gave a student a number for which string the bow is leaning toward, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 8. Bow speed (with direction)
<sub>bow_speed</sub>

This records how fast the bow is moving, and whether it is a down-bow or an up-bow. The number is zero when the bow is still, above zero for a down-bow and below zero for an up-bow; the bigger the number, the faster the bow. Teachers call this "bow speed".

**Question 1.** Do violin teachers pay attention to bow speed in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app gave a student a number for bow speed, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 9. Bow speed (without direction)
<sub>bow_speed_abs</sub>

This records how fast the bow is moving, without caring whether it is a down-bow or an up-bow. The number is zero when the bow is still, and the bigger the number, the faster the bow. Teachers call this "bow speed".

**Question 1.** Do violin teachers pay attention to bow speed regardless of direction in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app gave a student a number for bow speed regardless of direction, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 10. How quickly the bow speeds up or slows down
<sub>bow_accel</sub>

This records whether the bow is speeding up, slowing down, or keeping a steady speed during a stroke. The number is zero for a steady speed, and the bigger the number, the faster the speed is changing. Teachers talk about "speeding up" or "slowing down" the bow within a stroke.

**Question 1.** Do violin teachers pay attention to how quickly the bow speeds up or slows down in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app gave a student a number for how quickly the bow speeds up or slows down, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 11. Down-bow or up-bow
<sub>direction_sign</sub>

This records whether the bow is moving as a down-bow or an up-bow. The number is +1 for a clear down-bow, −1 for a clear up-bow, and near zero while the bow is stopped or turning around. Teachers say "down-bow" and "up-bow".

**Question 1.** Do violin teachers pay attention to whether the bow is going down or up in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app gave a student a number for whether the bow is going down or up, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 12. How bent the bow-arm elbow is
<sub>right_elbow_flexion_deg</sub>

This records how much the elbow of the bow arm is bent. The number is zero for a straight arm, and the bigger the number, the more the elbow is bent. Teachers talk about the "elbow" being too high or too low, and about "whole-arm strokes".

**Question 1.** Do violin teachers pay attention to how bent the bow-arm elbow is in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app gave a student a number for how bent the bow-arm elbow is, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 13. Bow-hand wrist turn, direction 1 of 3
<sub>right_wrist_aa_x_dev_deg</sub>

Our system watches the wrist of the bow hand and records how it is turned. It splits that turn into three directions, a bit like bending the wrist up and down, tilting it from side to side, and twisting it, though we cannot say exactly which direction is which. This card is about direction 1 of the three. The number is zero when the wrist is in the player's usual position, and it goes up or down as the wrist turns away from that. Teachers do not have a word for this; the closest is a "bent wrist".

**Question 1.** Do violin teachers pay attention to how the bow-hand wrist is turned in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app gave a student a number for how the bow-hand wrist is turned, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 14. Bow-hand wrist turn, direction 2 of 3
<sub>right_wrist_aa_y_dev_deg</sub>

Our system watches the wrist of the bow hand and records how it is turned. It splits that turn into three directions, a bit like bending the wrist up and down, tilting it from side to side, and twisting it, though we cannot say exactly which direction is which. This card is about direction 2 of the three. The number is zero when the wrist is in the player's usual position, and it goes up or down as the wrist turns away from that. Teachers do not have a word for this; the closest is a "bent wrist".

**Question 1.** Do violin teachers pay attention to how the bow-hand wrist is turned in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app gave a student a number for how the bow-hand wrist is turned, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 15. Bow-hand wrist turn, direction 3 of 3
<sub>right_wrist_aa_z_dev_deg</sub>

Our system watches the wrist of the bow hand and records how it is turned. It splits that turn into three directions, a bit like bending the wrist up and down, tilting it from side to side, and twisting it, though we cannot say exactly which direction is which. This card is about direction 3 of the three. The number is zero when the wrist is in the player's usual position, and it goes up or down as the wrist turns away from that. Teachers do not have a word for this; the closest is a "bent wrist".

**Question 1.** Do violin teachers pay attention to how the bow-hand wrist is turned in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app gave a student a number for how the bow-hand wrist is turned, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 16. Bow-arm shoulder position, compared with the player's usual
<sub>right_shoulder_rotation_dev_deg</sub>

This records how far the bow-arm shoulder has moved away from the position this player normally holds it in, for example when the shoulder rises or hunches. The number is zero in the usual position, and the bigger the number, the further the shoulder has moved. Teachers warn about a "raised shoulder".

**Question 1.** Do violin teachers pay attention to the bow-arm shoulder position in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app gave a student a number for the bow-arm shoulder position, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 17. Head tilt
<sub>neck_tilt_deg</sub>

This records how far the head is tilted away from upright, in any direction. The number is zero when the head is upright, and the bigger the number, the more it is tilted. Teachers talk about "head position".

**Question 1.** Do violin teachers pay attention to head tilt in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app gave a student a number for head tilt, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 18. Posture: upright or slouched
<sub>spine_curvature_deg</sub>

This records how much the upper body is bent forward or sideways instead of standing upright. The number is zero when upright, and the bigger the number, the more the body is bent. Teachers call this "posture" or "slouching".

**Question 1.** Do violin teachers pay attention to posture in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app gave a student a number for posture, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 19. How high the violin is held
<sub>violin_hold_height_ratio</sub>

This records how high the violin is held compared with the player's hips: lower when the scroll droops, higher when the violin is held up. The bigger the number, the higher the violin. Teachers warn about a "drooping scroll".

**Question 1.** Do violin teachers pay attention to how high the violin is held in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app gave a student a number for how high the violin is held, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 20. In tune, sharp, or flat
<sub>pitch_dev_semi</sub>

This records whether each note is in tune and, if not, how far off it is. The number is zero when the note is in tune, above zero when it is sharp (too high) and below zero when it is flat (too low). Teachers call this "intonation".

**Question 1.** Do violin teachers pay attention to whether a note is in tune, sharp or flat in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app gave a student a number for whether a note is in tune, sharp or flat, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 21. Loudness
<sub>env_db</sub>

This records how loud the playing is from moment to moment. The bigger the number, the louder the sound; very low numbers mean silence. Teachers talk about "dynamics" or "volume".

**Question 1.** Do violin teachers pay attention to loudness in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app gave a student a number for loudness, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 22. How strongly each note starts
<sub>onset_strength</sub>

This records how clearly and strongly each note starts. The number is high for a crisp, accented start and low in the middle of a long, held note. Teachers talk about the "attack" of a note.

**Question 1.** Do violin teachers pay attention to how strongly each note starts in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app gave a student a number for how strongly each note starts, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 23. The note being played
<sub>f0_midi</sub>

This records which note the violin is sounding at every moment, including the small wobbles of vibrato and the slides between notes. Higher numbers mean higher notes. Teachers talk about "the note you are playing".

**Question 1.** Do violin teachers pay attention to the note being played in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app gave a student a number for the note being played, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 24. How clean and clear the tone is
<sub>f0_salience</sub>

This records how clean and clear the tone is. The number is high for a clear, focused sound and low when the sound is scratchy, noisy, or silent. Teachers talk about a "clean tone" or a "scratchy tone".

**Question 1.** Do violin teachers pay attention to how clean and clear the tone is in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app gave a student a number for how clean and clear the tone is, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 25. Played on a different string than the music suggests
<sub>string_disagreement</sub>

This records whether a note was played on a different string from the one the sheet music suggests. The number is zero when it is the same string and 1 when it is clearly a different string; it is left blank when the music does not suggest a string. Teachers say "wrong string" or "play it on the A string".

**Question 1.** Do violin teachers pay attention to whether the player used a different string than the music suggests in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app gave a student a number for whether the player used a different string than the music suggests, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 26. Left-hand position, compared with what the music suggests
<sub>position_dev_semi</sub>

This records whether the left hand was higher or lower on the fingerboard than the sheet music suggests. The number is zero in the expected position, above zero when the hand is higher up and below zero when it is lower. Teachers talk about "positions" and "shifting".

**Question 1.** Do violin teachers pay attention to the left-hand position in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app gave a student a number for the left-hand position, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 27. The player's usual bow-contact spot
<sub>contact_bridge_ratio_neutral</sub>

This records where the bow usually touches the string over a whole recording, between the bridge and the fingerboard. The number is zero at the bridge, and the bigger the number, the closer to the fingerboard. Teachers call this spot the "sounding point" or "contact point".

**Question 1.** Do violin teachers pay attention to the player's usual bow-contact spot in lessons?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app gave a student a number for the player's usual bow-contact spot, could the student act on it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

