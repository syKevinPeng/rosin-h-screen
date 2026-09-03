# Atom audit · round 0: incumbent atoms

**form version:** `7830e9e9f3a7` · **rater:** ☐ the violinist · ☐ the author (Siyuan)

Printable form (paper fallback): cards in fixed order, tick one box per question.

27 short cards. Each one describes a single thing our system measures from a violin performance (we call it an "atom"). Rate each card on two questions and add a note if you like. There are no right answers; we want your judgment as a teacher.

## The two questions

**H1.** Is this something violin teachers actually attend to in lessons?

**H2.** If a tutor reported this value to a student, could the student act on it?  
*The number itself, not the concept: for example "your bow speed varied a lot in this phrase", as opposed to a quantity that no instruction maps to.*

## The scale (no midpoint, on purpose)

- **1** clearly no
- **2** probably no
- **3** probably yes
- **4** clearly yes

---

### 1. Bow speed, with direction
`bow_speed`  
**Calibration example: rate it like any other card.**

**How teachers say it:**
- bow speed · attributed to: Fischer, The Violin Lesson (2013); Flesch, The Art of Violin Playing, Book 1
- It is impossible to scratch if the bow keeps moving · quoted from: Fischer, The Violin Lesson (2013), chapter heading
- evenness, accuracy, beauty (Lin Yaoji's three-word maxim, translated) · quoted from: Lin Yaoji, teaching maxim, in Yang Baozhi, Essentials of Lin Yaoji's Violin Teaching Method (2004)

**What it measures:** How fast the bow is moving along the string, with the sign showing whether it is a down-bow or an up-bow.  
**Unit:** bow-hair lengths per second, so 1 means a whole bow in one second  
**Range:** 0 = bow stopped; positive = down-bow (toward the tip); negative = up-bow

**H1.** Is this something violin teachers actually attend to in lessons?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**H2.** If a tutor reported this value to a student, could the student act on it?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 2. Right-wrist rotation, model axis Z, relative to the player's usual
`right_wrist_aa_z_dev_deg`  
**Calibration example: rate it like any other card.**

**How teachers say it:**
- bent wrist · attributed to: Rolland, The Teaching of Action in String Playing (1974)
- wrist flexion at the frog · expert spreadsheet:: ViolinITS schema leaf
- how the wrist is turned about the model's Z axis · paraphrase, uncited

**What it measures:** One of three parts of how the bow-hand wrist is turned, taken about the motion-capture model's Z axis, compared with this player's usual wrist posture in that recording. The three axes are the model's axes, not anatomical names such as flexion or deviation.  
**Unit:** degrees  
**Range:** 0 = the player's usual wrist posture in the recording; positive or negative = turned one way or the other about that axis

**H1.** Is this something violin teachers actually attend to in lessons?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**H2.** If a tutor reported this value to a student, could the student act on it?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 3. Contact point, relative to the player's usual
`contact_bridge_ratio_dev`

**How teachers say it:**
- soundpoint / the five soundpoints · attributed to: Fischer, The Violin Lesson (2013)
- contact point · attributed to: Flesch, The Art of Violin Playing, Book 1
- the bow drifting from the contact point · attributed to: Starr, The Suzuki Violinist
- evenness (from Lin Yaoji's maxim: evenness, accuracy, beauty; translated) · quoted from: Lin Yaoji, teaching maxim, in Yang Baozhi, Essentials of Lin Yaoji's Violin Teaching Method (2004)

**What it measures:** Where the bow hair touches the string between the bridge and the fingerboard, compared with the player's own usual contact point in that recording.  
**Unit:** a fraction of the string length (bridge to nut)  
**Range:** 0 = the player's usual point; negative = closer to the bridge than usual; positive = closer to the fingerboard than usual

**H1.** Is this something violin teachers actually attend to in lessons?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**H2.** If a tutor reported this value to a student, could the student act on it?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 4. Position along the bow, frog to tip
`hair_pos`

**How teachers say it:**
- at the frog / in the middle / at the tip · paraphrase, uncited
- bow distribution · expert spreadsheet:: ViolinITS etude classification spreadsheet, columns "Equal length, 2 bow length, 3-4 bow length"
- whole bows · attributed to: Fischer, The Violin Lesson (2013)

**What it measures:** Which part of the bow hair is on the string at that moment, from the frog to the tip.  
**Unit:** a fraction of the bow-hair length  
**Range:** 0 = at the frog; 0.5 = the middle of the bow; 1 = at the tip

**H1.** Is this something violin teachers actually attend to in lessons?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**H2.** If a tutor reported this value to a student, could the student act on it?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 5. Bow-to-string gap, on or off the string
`hair_string_gap_ratio`

**How teachers say it:**
- bow on the string / off the string · paraphrase, uncited
- Sautillé & Spiccato, Ricochet, Flying staccato (off-string strokes) · expert spreadsheet:: ViolinITS etude classification spreadsheet

**What it measures:** How far the bow hair is from the string: zero when the bow is on the string, larger when it is lifted off.  
**Unit:** a fraction of the string length  
**Range:** 0 = hair on the string; larger = further off the string

**H1.** Is this something violin teachers actually attend to in lessons?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**H2.** If a tutor reported this value to a student, could the student act on it?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 6. Bow skew: straight versus crooked bow
`skew_deg`

**How teachers say it:**
- crooked bow · attributed to: Hamann & Gillespie, Strategies for Teaching Strings (4th ed., 2018)
- keep the bow straight · paraphrase, uncited
- bow–string angle · measurement study:: Provenzale et al. (2024), Sensors

**What it measures:** How far the bow is from being at a right angle to the string, that is, how crooked the bow is.  
**Unit:** degrees  
**Range:** 0 = perfectly straight bow; larger = more crooked, whichever way it leans

**H1.** Is this something violin teachers actually attend to in lessons?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**H2.** If a tutor reported this value to a student, could the student act on it?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 7. Bow tilt around the string: which string the bow is on
`string_side_deg`

**How teachers say it:**
- string crossing · attributed to: Galamian, Principles of Violin Playing and Teaching (1962); Rolland, The Teaching of Action in String Playing (1974)
- bow tilt · measurement study:: Provenzale et al. (2024), Sensors
- string level · paraphrase, uncited

**What it measures:** The angle at which the bow sits around the string, which shows which string the bow is leaning toward, measured against the violin body.  
**Unit:** degrees  
**Range:** an angle; smaller toward the G-string side, larger toward the E-string side

**H1.** Is this something violin teachers actually attend to in lessons?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**H2.** If a tutor reported this value to a student, could the student act on it?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 8. Bow speed, with direction
`bow_speed`

**How teachers say it:**
- bow speed · attributed to: Fischer, The Violin Lesson (2013); Flesch, The Art of Violin Playing, Book 1
- It is impossible to scratch if the bow keeps moving · quoted from: Fischer, The Violin Lesson (2013), chapter heading
- evenness, accuracy, beauty (Lin Yaoji's three-word maxim, translated) · quoted from: Lin Yaoji, teaching maxim, in Yang Baozhi, Essentials of Lin Yaoji's Violin Teaching Method (2004)

**What it measures:** How fast the bow is moving along the string, with the sign showing whether it is a down-bow or an up-bow.  
**Unit:** bow-hair lengths per second, so 1 means a whole bow in one second  
**Range:** 0 = bow stopped; positive = down-bow (toward the tip); negative = up-bow

**H1.** Is this something violin teachers actually attend to in lessons?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**H2.** If a tutor reported this value to a student, could the student act on it?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 9. Bow speed: how fast, regardless of direction
`bow_speed_abs`

**How teachers say it:**
- bow speed · attributed to: Fischer, The Violin Lesson (2013); Flesch, The Art of Violin Playing, Book 1
- the bow keeps moving · quoted from: Fischer, The Violin Lesson (2013), chapter heading

**What it measures:** How fast the bow is moving, regardless of whether it is a down-bow or an up-bow.  
**Unit:** bow-hair lengths per second  
**Range:** 0 = stopped; 1 = a whole bow in one second; larger = faster

**H1.** Is this something violin teachers actually attend to in lessons?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**H2.** If a tutor reported this value to a student, could the student act on it?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 10. Bow acceleration
`bow_accel`

**How teachers say it:**
- speeding up or slowing down the bow within a stroke · paraphrase, uncited
- Martelé & Marcato, Accent (accented strokes) · expert spreadsheet:: ViolinITS etude classification spreadsheet

**What it measures:** How quickly the bow is speeding up or slowing down within a stroke.  
**Unit:** change in bow speed per second  
**Range:** 0 = steady speed; larger = the speed is changing faster; the sign follows the down-bow-positive convention

**H1.** Is this something violin teachers actually attend to in lessons?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**H2.** If a tutor reported this value to a student, could the student act on it?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 11. Bow direction: down-bow or up-bow
`direction_sign`

**How teachers say it:**
- down-bow / up-bow · paraphrase, uncited

**What it measures:** Whether the bow is moving as a down-bow or an up-bow, as a smooth value that passes through zero when the bow changes direction.  
**Unit:** a sign from −1 to +1  
**Range:** +1 = clearly down-bow; −1 = clearly up-bow; near 0 = stopped or changing direction

**H1.** Is this something violin teachers actually attend to in lessons?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**H2.** If a tutor reported this value to a student, could the student act on it?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 12. Right elbow bend (bow arm)
`right_elbow_flexion_deg`

**How teachers say it:**
- elbow angle / elbow height of the bow arm · paraphrase, uncited
- whole-arm strokes · attributed to: Rolland, The Teaching of Action in String Playing (1974); Galamian, Principles (1962)
- changing notes without changing the arm shape · attributed to: Lin Yaoji, in Yang Baozhi (2004); English rendering only in our reading notes

**What it measures:** How much the bow-arm elbow is bent, measured from the motion-capture model's straight-arm reference.  
**Unit:** degrees of rotation from the reference pose, not a clinically calibrated joint angle  
**Range:** 0 = arm straight in the reference pose; larger = more bent

**H1.** Is this something violin teachers actually attend to in lessons?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**H2.** If a tutor reported this value to a student, could the student act on it?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 13. Right-wrist rotation, model axis X, relative to the player's usual
`right_wrist_aa_x_dev_deg`

**How teachers say it:**
- bent wrist · attributed to: Rolland, The Teaching of Action in String Playing (1974)
- wrist flexion at the frog · expert spreadsheet:: ViolinITS schema leaf
- how the wrist is turned about the model's X axis · paraphrase, uncited

**What it measures:** One of three parts of how the bow-hand wrist is turned, taken about the motion-capture model's X axis, compared with this player's usual wrist posture in that recording. The three axes are the model's axes, not anatomical names such as flexion or deviation.  
**Unit:** degrees  
**Range:** 0 = the player's usual wrist posture in the recording; positive or negative = turned one way or the other about that axis

**H1.** Is this something violin teachers actually attend to in lessons?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**H2.** If a tutor reported this value to a student, could the student act on it?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 14. Right-wrist rotation, model axis Y, relative to the player's usual
`right_wrist_aa_y_dev_deg`

**How teachers say it:**
- bent wrist · attributed to: Rolland, The Teaching of Action in String Playing (1974)
- wrist flexion at the frog · expert spreadsheet:: ViolinITS schema leaf
- how the wrist is turned about the model's Y axis · paraphrase, uncited

**What it measures:** One of three parts of how the bow-hand wrist is turned, taken about the motion-capture model's Y axis, compared with this player's usual wrist posture in that recording. The three axes are the model's axes, not anatomical names such as flexion or deviation.  
**Unit:** degrees  
**Range:** 0 = the player's usual wrist posture in the recording; positive or negative = turned one way or the other about that axis

**H1.** Is this something violin teachers actually attend to in lessons?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**H2.** If a tutor reported this value to a student, could the student act on it?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 15. Right-wrist rotation, model axis Z, relative to the player's usual
`right_wrist_aa_z_dev_deg`

**How teachers say it:**
- bent wrist · attributed to: Rolland, The Teaching of Action in String Playing (1974)
- wrist flexion at the frog · expert spreadsheet:: ViolinITS schema leaf
- how the wrist is turned about the model's Z axis · paraphrase, uncited

**What it measures:** One of three parts of how the bow-hand wrist is turned, taken about the motion-capture model's Z axis, compared with this player's usual wrist posture in that recording. The three axes are the model's axes, not anatomical names such as flexion or deviation.  
**Unit:** degrees  
**Range:** 0 = the player's usual wrist posture in the recording; positive or negative = turned one way or the other about that axis

**H1.** Is this something violin teachers actually attend to in lessons?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**H2.** If a tutor reported this value to a student, could the student act on it?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 16. Right shoulder rotation, relative to the player's usual
`right_shoulder_rotation_dev_deg`

**How teachers say it:**
- raised shoulder · attributed to: Rolland, The Teaching of Action in String Playing (1974)
- gripping / clamping · attributed to: Havas, A New Approach to Violin Playing (1961)
- let the violin become part of the body (translated) · quoted from: Lin Yaoji, in Yang Baozhi, Essentials of Lin Yaoji's Violin Teaching Method (2004)

**What it measures:** How much the bow-arm shoulder is turned, compared with this player's usual shoulder position in that recording, in any direction.  
**Unit:** degrees of rotation, not a clinically calibrated joint angle  
**Range:** 0 = the usual shoulder position; larger = further from it

**H1.** Is this something violin teachers actually attend to in lessons?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**H2.** If a tutor reported this value to a student, could the student act on it?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 17. Head and neck tilt
`neck_tilt_deg`

**How teachers say it:**
- head position / head tilt · paraphrase, uncited
- chin / jaw pressure · expert spreadsheet:: ViolinITS schema leaf
- Analysis and correction of common posture errors in violin study (article title, translated) · quoted from: Yang Lingchao (2001), article title

**What it measures:** How far the head and neck are tilted away from the motion-capture model's upright reference, in any direction.  
**Unit:** degrees  
**Range:** 0 = the upright reference; larger = more tilted

**H1.** Is this something violin teachers actually attend to in lessons?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**H2.** If a tutor reported this value to a student, could the student act on it?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 18. Spine curvature: upright versus slouched
`spine_curvature_deg`

**How teachers say it:**
- posture · attributed to: Kreitman, Teaching from the Balance Point (1998); Flesch, The Art of Violin Playing, Book 1; Gruenberg (1919)
- balanced stance · attributed to: Rolland, The Teaching of Action in String Playing (1974)
- slouching · paraphrase, uncited

**What it measures:** How far the upper body is bent away from the motion-capture model's upright reference, combining the three spine joints.  
**Unit:** degrees  
**Range:** 0 = the upright reference; larger = more curved

**H1.** Is this something violin teachers actually attend to in lessons?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**H2.** If a tutor reported this value to a student, could the student act on it?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 19. Violin hold height
`violin_hold_height_ratio`

**How teachers say it:**
- scroll drooping · attributed to: Auer, Violin Playing as I Teach It (1921)
- violin drifting over the right arm · attributed to: Starr, The Suzuki Violinist
- instrument support · attributed to: Rolland, The Teaching of Action in String Playing (1974)
- let the violin become part of the body (translated) · quoted from: Lin Yaoji, in Yang Baozhi, Essentials of Lin Yaoji's Violin Teaching Method (2004)

**What it measures:** How high the violin's bridge sits above the player's hips, so a drooping violin gives a smaller value and a well-raised one a larger value.  
**Unit:** a fraction of the string length, so it does not depend on body size  
**Range:** larger = the violin is held higher relative to the hips

**H1.** Is this something violin teachers actually attend to in lessons?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**H2.** If a tutor reported this value to a student, could the student act on it?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 20. Intonation error: sharp or flat · *incoming (v18)*
`pitch_dev_semi`

**How teachers say it:**
- constant adjustment · quoted from: Galamian, Principles of Violin Playing and Teaching (1962)
- Intonation · attributed to: Fischer, Basics (1997), section F heading
- sharp / flat · measurement study:: feedback wording in the experimental literature (Salzberg 1980)
- intonation (the standard Chinese pedagogical term, translated) · quoted from: Xiao Ke (2016); Ma Xishui (2002), article titles
- accuracy (from Lin Yaoji's maxim: evenness, accuracy, beauty; translated) · quoted from: Lin Yaoji, teaching maxim, in Yang Baozhi, Essentials of Lin Yaoji's Violin Teaching Method (2004)

**What it measures:** How far the pitch actually played is from the written pitch of the note.  
**Unit:** semitones; 100 cents make one semitone  
**Range:** 0 = exactly the written pitch; positive = sharp; negative = flat; 0.5 = a quarter-tone off

**H1.** Is this something violin teachers actually attend to in lessons?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**H2.** If a tutor reported this value to a student, could the student act on it?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 21. Loudness
`env_db`

**How teachers say it:**
- dynamics (No dynamics, Simple Dynamics, Inter. dynamics) · expert spreadsheet:: ViolinITS etude classification spreadsheet, "Tone" columns
- nuance · attributed to: Auer, Violin Playing as I Teach It (1921), chapter topic
- volume / a bigger sound · paraphrase, uncited

**What it measures:** How loud the sound is at each moment, as the ear would hear it rise and fall.  
**Unit:** decibels, a log scale of sound level  
**Range:** higher = louder; very low = silence

**H1.** Is this something violin teachers actually attend to in lessons?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**H2.** If a tutor reported this value to a student, could the student act on it?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 22. Note attack strength
`onset_strength`

**How teachers say it:**
- articulation · measurement study:: Cavitt (2003), teacher correction targets (band rehearsals)
- Accent / Sfz, Martelé & Marcato · expert spreadsheet:: ViolinITS etude classification spreadsheet, "Bow strokes" columns
- key bow strokes · attributed to: Fischer, Basics (1997), section C
- attack / the start of the note · paraphrase, uncited

**What it measures:** How strongly a new note is beginning at each moment: high at a clear, accented attack, low in the middle of a sustained note.  
**Unit:** an attack-strength score with no physical unit  
**Range:** 0 = no new note starting; larger = a stronger, sharper attack

**H1.** Is this something violin teachers actually attend to in lessons?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**H2.** If a tutor reported this value to a student, could the student act on it?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 23. Pitch being played
`f0_midi`

**How teachers say it:**
- constant adjustment · quoted from: Galamian, Principles of Violin Playing and Teaching (1962)
- flat 3rd finger · attributed to: Hamann & Gillespie, Strategies for Teaching Strings (4th ed., 2018)
- accuracy (from Lin Yaoji's maxim: evenness, accuracy, beauty; translated) · quoted from: Lin Yaoji, teaching maxim, in Yang Baozhi, Essentials of Lin Yaoji's Violin Teaching Method (2004)
- intonation (the standard Chinese pedagogical term, translated) · quoted from: Xiao Ke (2016); Ma Xishui (2002), article titles
- the note you are playing · paraphrase, uncited

**What it measures:** The pitch the violin is sounding at each moment, tracked continuously, so vibrato, slides and out-of-tune notes all show.  
**Unit:** piano-key numbers with fractions; a step of 1 is one semitone  
**Range:** higher = higher pitch, over the violin's range from the open G string upward

**H1.** Is this something violin teachers actually attend to in lessons?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**H2.** If a tutor reported this value to a student, could the student act on it?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 24. Pitch clarity: how clearly a pitch is present
`f0_salience`

**How teachers say it:**
- It is impossible to scratch if the bow keeps moving · quoted from: Fischer, The Violin Lesson (2013), chapter heading
- scratchy tone · attributed to: Hamann & Gillespie, Strategies for Teaching Strings (4th ed., 2018)
- tonalization · quoted from: Suzuki, as described in Starr, The Suzuki Violinist
- evenness, beauty (from Lin Yaoji's three-word maxim, translated) · quoted from: Lin Yaoji, teaching maxim, in Yang Baozhi, Essentials of Lin Yaoji's Violin Teaching Method (2004)
- clean, focused tone · paraphrase, uncited

**What it measures:** How clearly a definite pitch is present in the sound at each moment: high for a clean, focused tone, low for scratch, noise or silence.  
**Unit:** a pitch-evidence score with no physical unit  
**Range:** near 0 = no clear pitch (silence or noise); larger = a clearer, more focused pitch

**H1.** Is this something violin teachers actually attend to in lessons?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**H2.** If a tutor reported this value to a student, could the student act on it?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 25. Played on a different string than the score implies
`string_disagreement`

**How teachers say it:**
- wrong string / play it on the A string · paraphrase, uncited
- String/s · expert spreadsheet:: ViolinITS etude classification spreadsheet, metadata column
- building stepwise fingers on one string (D) · expert spreadsheet:: ViolinITS etude classification spreadsheet, goal text

**What it measures:** How strongly the evidence from the sound and the left hand says the note was played on a different string from the one the written music implies.  
**Unit:** a score from 0 to 1  
**Range:** 0 = the same string as the score implies; 1 = clearly a different string; blank when the score gives no usable string

**H1.** Is this something violin teachers actually attend to in lessons?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**H2.** If a tutor reported this value to a student, could the student act on it?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 26. Left-hand position, compared with what the score implies
`position_dev_semi`

**How teachers say it:**
- position changing · attributed to: Fischer, The Violin Lesson (2013), lesson topic; Fischer, Basics (1997), section E "Shifting"
- Position, Small Shifting · expert spreadsheet:: ViolinITS etude classification spreadsheet, "Hand Frame" columns
- missed shift · attributed to: Gerle, The Art of Practising the Violin (1983)
- shifting / hand frame (translated terms) · quoted from: Ding Zhinuo, Intensive Training Materials for Violin Fundamentals (Shanghai Music Publishing House)
- stay in third position · paraphrase, uncited

**What it measures:** Where on the fingerboard the left hand actually was for the note, compared with the position the written music implies.  
**Unit:** semitones along the string  
**Range:** 0 = the position the score implies; positive = higher up the fingerboard than implied; negative = lower

**H1.** Is this something violin teachers actually attend to in lessons?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**H2.** If a tutor reported this value to a student, could the student act on it?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

### 27. The player's habitual sounding point
`contact_bridge_ratio_neutral`

**How teachers say it:**
- soundpoint / the five soundpoints · attributed to: Fischer, The Violin Lesson (2013)
- contact point · attributed to: Flesch, The Art of Violin Playing, Book 1
- the bow drifting from the contact point · attributed to: Starr, The Suzuki Violinist
- evenness (from Lin Yaoji's maxim: evenness, accuracy, beauty; translated) · quoted from: Lin Yaoji, teaching maxim, in Yang Baozhi, Essentials of Lin Yaoji's Violin Teaching Method (2004)
- playing too close to the fingerboard / too close to the bridge · paraphrase, uncited

**What it measures:** The player's usual contact point in that recording: where along the string the bow hair most often sits, between the bridge and the fingerboard.  
**Unit:** a fraction of the string length (bridge to nut)  
**Range:** 0 = at the bridge; larger = further toward the fingerboard; one value per recording, not per moment

**H1.** Is this something violin teachers actually attend to in lessons?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**H2.** If a tutor reported this value to a student, could the student act on it?  
☐ 1 clearly no · ☐ 2 probably no · ☐ 3 probably yes · ☐ 4 clearly yes

**Notes (optional): how would you say this to a student? Anything unclear?**  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

