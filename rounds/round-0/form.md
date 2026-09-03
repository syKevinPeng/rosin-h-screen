# Violin teaching survey · round 0

**form version:** `d262d26a4770` · **rater:** ☐ the violinist · ☐ the author (Siyuan)

Paper version: cards in a fixed order, tick one box per question.

We built a computer program that watches and listens to someone playing the violin and keeps track of many things about the playing. You will see 27 short cards; each describes one of those things in everyday words, and two of them appear twice, once as a warm-up. For each card, tell us two things: do violin teachers care about it, and could a student use the number? There are no right or wrong answers.

## The two questions

**Question 1.** In lessons, do violin teachers pay attention to this?

**Question 2.** If a practice app showed a student this number, could the student do something about it?  
*We mean this card's number. Could a student practise differently because of it?*

## How to answer

- **1** definitely not
- **2** probably not
- **3** probably yes
- **4** definitely yes

---

### 1. Bow speed (with direction)
<sub>bow_speed</sub>  
**Warm-up card: answer it like any other.**

This records how fast the bow is moving, and whether it is a down-bow or an up-bow. The number is zero when the bow is still, above zero for a down-bow and below zero for an up-bow; the bigger the number, the faster the bow. Teachers call this "bow speed". (Two related cards ask about speed alone and about direction alone.)

**Question 1.** In lessons, do violin teachers pay attention to bow speed?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app showed a student this number, could the student do something about it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 2. Bow-hand wrist: bending up and down
<sub>right_wrist_aa_z_dev_deg</sub>  
**Warm-up card: answer it like any other.**

Our program watches the wrist of the bow hand and records how it is turned, split into three movements: twisting, tilting from side to side, and bending up and down (see the picture). This card is about how the wrist bends up and down. The number is zero at the player's usual position and goes above or below zero as it moves one way or the other; the further from zero, the bigger the change. We could not find a teacher's word for this exact movement; the closest is a "bent wrist".

**Question 1.** In lessons, do violin teachers pay attention to how the bow-hand wrist bends up and down?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app showed a student this number, could the student do something about it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 3. Where the bow touches the string, compared with the player's usual spot
<sub>contact_bridge_ratio_dev</sub>

This records where the bow touches the string and compares it with the spot this player normally uses. The number is zero at the usual spot, below zero when the bow is nearer the bridge than usual, and above zero when it is nearer the fingerboard. Teachers call this spot the "sounding point" or "contact point". (A separate card asks about the player's usual spot itself; this one is about moment-to-moment changes away from it.)

**Question 1.** In lessons, do violin teachers pay attention to where the bow touches the string?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app showed a student this number, could the student do something about it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 4. Which part of the bow is on the string
<sub>hair_pos</sub>

This records which part of the bow is on the string: near the hand end (the frog), the middle, or the tip. The number is 0 at the frog, 0.5 in the middle and 1 at the tip. Teachers talk about "bow distribution" and "whole bows"; you might hear "at the frog" or "at the tip".

**Question 1.** In lessons, do violin teachers pay attention to which part of the bow is on the string?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app showed a student this number, could the student do something about it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 5. Is the bow on the string or lifted off?
<sub>hair_string_gap_ratio</sub>

This records whether the bow is touching the string or lifted off it. The number is zero when the bow is on the string and grows as the bow lifts higher. You might hear this described as playing "on the string" or "off the string"; teachers name off-the-string strokes such as spiccato.

**Question 1.** In lessons, do violin teachers pay attention to whether the bow is on the string or lifted off?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app showed a student this number, could the student do something about it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 6. Is the bow straight or crooked?
<sub>skew_deg</sub>

This records whether the bow is straight or crooked, in other words whether it crosses the strings at a right angle. The number is zero for a perfectly straight bow and grows as the bow gets more crooked. Teachers diagnose a "crooked bow"; you might hear "keep the bow straight".

**Question 1.** In lessons, do violin teachers pay attention to how straight the bow is?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app showed a student this number, could the student do something about it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 7. Which string the bow is leaning toward
<sub>string_side_deg</sub>

This records which string the bow is leaning toward. Lower numbers mean the bow is leaning toward the G string, the lowest one; higher numbers mean toward the E string, the highest one. Teachers talk about "string crossing".

**Question 1.** In lessons, do violin teachers pay attention to which string the bow is leaning toward?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app showed a student this number, could the student do something about it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 8. Bow speed (with direction)
<sub>bow_speed</sub>

This records how fast the bow is moving, and whether it is a down-bow or an up-bow. The number is zero when the bow is still, above zero for a down-bow and below zero for an up-bow; the bigger the number, the faster the bow. Teachers call this "bow speed". (Two related cards ask about speed alone and about direction alone.)

**Question 1.** In lessons, do violin teachers pay attention to bow speed?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app showed a student this number, could the student do something about it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 9. Bow speed (without direction)
<sub>bow_speed_abs</sub>

This records how fast the bow is moving, without caring whether it is a down-bow or an up-bow. The number is zero when the bow is still, and the bigger the number, the faster the bow. Teachers call this "bow speed". (A related card keeps the direction as well.)

**Question 1.** In lessons, do violin teachers pay attention to bow speed regardless of direction?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app showed a student this number, could the student do something about it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 10. How quickly the bow speeds up or slows down
<sub>bow_accel</sub>

This records whether the bow is speeding up, slowing down, or keeping a steady speed during a stroke. The number is zero for a steady speed and goes above or below zero as the speed changes one way or the other; the further from zero, the quicker the change. You might hear this described as "speeding up" or "slowing down" the bow within a stroke.

**Question 1.** In lessons, do violin teachers pay attention to how quickly the bow speeds up or slows down?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app showed a student this number, could the student do something about it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 11. Down-bow or up-bow
<sub>direction_sign</sub>

This records whether the bow is moving as a down-bow or an up-bow. The number is +1 for a clear down-bow, −1 for a clear up-bow, and near zero while the bow is stopped or turning around. You might hear simply "down-bow" and "up-bow".

**Question 1.** In lessons, do violin teachers pay attention to whether the bow is going down or up?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app showed a student this number, could the student do something about it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 12. How bent the bow-arm elbow is
<sub>right_elbow_flexion_deg</sub>

This records how much the elbow of the bow arm is bent. The number is zero for a straight arm, and the bigger the number, the more the elbow is bent. Teachers talk about "whole-arm strokes"; you might hear the elbow described as too high or too low.

**Question 1.** In lessons, do violin teachers pay attention to how bent the bow-arm elbow is?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app showed a student this number, could the student do something about it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 13. Bow-hand wrist: twisting
<sub>right_wrist_aa_x_dev_deg</sub>

Our program watches the wrist of the bow hand and records how it is turned, split into three movements: twisting, tilting from side to side, and bending up and down (see the picture). This card is about how the wrist twists. The number is zero at the player's usual position and goes above or below zero as it moves one way or the other; the further from zero, the bigger the change. We could not find a teacher's word for this exact movement; the closest is a "bent wrist".

**Question 1.** In lessons, do violin teachers pay attention to how the bow-hand wrist twists?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app showed a student this number, could the student do something about it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 14. Bow-hand wrist: tilting from side to side
<sub>right_wrist_aa_y_dev_deg</sub>

Our program watches the wrist of the bow hand and records how it is turned, split into three movements: twisting, tilting from side to side, and bending up and down (see the picture). This card is about how the wrist tilts from side to side. The number is zero at the player's usual position and goes above or below zero as it moves one way or the other; the further from zero, the bigger the change. We could not find a teacher's word for this exact movement; the closest is a "bent wrist".

**Question 1.** In lessons, do violin teachers pay attention to how the bow-hand wrist tilts from side to side?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app showed a student this number, could the student do something about it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 15. Bow-hand wrist: bending up and down
<sub>right_wrist_aa_z_dev_deg</sub>

Our program watches the wrist of the bow hand and records how it is turned, split into three movements: twisting, tilting from side to side, and bending up and down (see the picture). This card is about how the wrist bends up and down. The number is zero at the player's usual position and goes above or below zero as it moves one way or the other; the further from zero, the bigger the change. We could not find a teacher's word for this exact movement; the closest is a "bent wrist".

**Question 1.** In lessons, do violin teachers pay attention to how the bow-hand wrist bends up and down?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app showed a student this number, could the student do something about it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 16. How the bow arm is turned or lifted at the shoulder
<sub>right_shoulder_rotation_dev_deg</sub>

This records how much the bow arm is turned or lifted at the shoulder joint, compared with the way this player usually holds it. The number is zero at the player's usual position and goes above or below zero as it moves one way or the other; the further from zero, the bigger the change. Teachers talk about the height of the bow arm; the nearest common warning is a "raised shoulder".

**Question 1.** In lessons, do violin teachers pay attention to how the bow arm is turned or lifted at the shoulder?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app showed a student this number, could the student do something about it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 17. Head tilt or turn
<sub>neck_tilt_deg</sub>

This records how far the head is tilted or turned away from facing straight ahead and upright, in any direction. The number is zero when the head is upright and facing forward, and the bigger the number, the more it is tilted or turned. You might hear this described as "head position".

**Question 1.** In lessons, do violin teachers pay attention to head tilt or turn?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app showed a student this number, could the student do something about it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 18. Posture: upright or slouched
<sub>spine_curvature_deg</sub>

This records how much the upper body is bent forward or sideways instead of standing upright. The number is zero when upright, and the bigger the number, the more the body is bent. Teachers call this "posture" or "slouching".

**Question 1.** In lessons, do violin teachers pay attention to posture?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app showed a student this number, could the student do something about it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 19. How high the violin is held
<sub>violin_hold_height_ratio</sub>

This records how high the violin sits above the player's hips, measured at the bridge, the small wooden piece under the strings. The bigger the number, the higher the whole violin is held. Teachers talk about "holding the violin up".

**Question 1.** In lessons, do violin teachers pay attention to how high the violin is held?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app showed a student this number, could the student do something about it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 20. In tune, sharp, or flat
<sub>pitch_dev_semi</sub>

This records whether each note is in tune and, if not, how far off it is. The number is zero when the note is in tune, above zero when it is sharp (too high) and below zero when it is flat (too low). Teachers call this "intonation".

**Question 1.** In lessons, do violin teachers pay attention to whether a note is in tune, sharp or flat?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app showed a student this number, could the student do something about it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 21. Loudness
<sub>env_db</sub>

This records how loud the playing is from moment to moment. The bigger the number, the louder the sound; very low numbers mean silence. Teachers talk about "dynamics" or "volume".

**Question 1.** In lessons, do violin teachers pay attention to loudness?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app showed a student this number, could the student do something about it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 22. How strongly each note starts
<sub>onset_strength</sub>

This records how clearly and strongly each note starts. The number is high for a crisp, accented start and low in the middle of a long, held note. Teachers talk about "articulation" and accented strokes; you might hear it called the "attack" of a note.

**Question 1.** In lessons, do violin teachers pay attention to how strongly each note starts?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app showed a student this number, could the student do something about it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 23. The note being played
<sub>f0_midi</sub>

This records which note the violin is sounding at every moment, including the small wobbles of vibrato and the slides between notes. Higher numbers mean higher notes. Teachers talk about "intonation" and "constant adjustment" of the note being played.

**Question 1.** In lessons, do violin teachers pay attention to the note being played?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app showed a student this number, could the student do something about it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 24. Whether a clear note can be heard
<sub>f0_salience</sub>

This records how strongly a definite note can be heard in the sound at each moment. The number is high when a clear note is sounding and low when there is silence, noise, or no clear pitch, for example a scratchy moment. Teachers speak of a "scratchy tone"; one teacher's rule is that "it is impossible to scratch if the bow keeps moving".

**Question 1.** In lessons, do violin teachers pay attention to whether a clear note can be heard?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app showed a student this number, could the student do something about it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 25. Played on a string that could not produce the written note
<sub>string_disagreement</sub>

This records whether a note seems to have been played on a string that could not produce the note written in the music, judging from the sound and the left hand. The number is zero when the string used could play the written note and 1 when it clearly could not; it is left blank when the music does not say which notes are possible. The nearest thing a teacher says is "wrong string".

**Question 1.** In lessons, do violin teachers pay attention to playing a note on a string that could not produce the written note?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app showed a student this number, could the student do something about it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 26. Left-hand position, compared with what the music suggests
<sub>position_dev_semi</sub>

This records whether the left hand was higher or lower on the fingerboard than the sheet music suggests. The number is zero in the expected position, above zero when the hand is higher up and below zero when it is lower. Teachers talk about "positions" and "shifting".

**Question 1.** In lessons, do violin teachers pay attention to the left-hand position?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app showed a student this number, could the student do something about it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 27. The player's usual bow-contact spot
<sub>contact_bridge_ratio_neutral</sub>

This records where the bow usually touches the string over a whole recording, between the bridge and the fingerboard. The number is zero at the bridge, and the bigger the number, the closer to the fingerboard. Teachers call this spot the "sounding point" or "contact point". (A separate card asks about moment-to-moment changes away from this spot; this one is about the usual spot itself.)

**Question 1.** In lessons, do violin teachers pay attention to the player's usual bow-contact spot?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Question 2.** If a practice app showed a student this number, could the student do something about it?  
☐ 1 definitely not · ☐ 2 probably not · ☐ 3 probably yes · ☐ 4 definitely yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

