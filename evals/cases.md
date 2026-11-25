# Behavioral evaluation cases

Start in an empty project directory. Give the agent the request, source material, and this skill. Keep the actual outputs for inspection. Grade visual evidence from the current image. Use **Unclear** when a required detail cannot be seen. To compare versions or assess the skill's contribution, use the same host and source material in runs with and without the skill.

| Task | Request and materials | Evidence to inspect |
| --- | --- | --- |
| Single descriptive illustration | Illustrate “The tide had just gone out. A single white shell lay on the lowest of the gray stone steps.” Make a landscape-format illustration without lettering. | Open the image. Check the shell's number, color, position on the steps, and relationship to the waterline. Check for unsupported figures, signs, or editorial decoration. |
| Transfer of an object and passage of time | “As Ye He came through the door, she held a brass button tight in her hand. She put it in an empty saucer, turned, and left. Only after dark did A-Dong carry the saucer away.” Deliver a three-image storyboard and a self-contained generation prompt for each image. | Trace who holds the button, the state of the saucer, and the timing of A-Dong's appearance. The button and saucer remain identifiable. Each prompt depicts one moment. |
| Revision of an existing image | Set “The tide had just gone out.” as a caption on the artwork from the first case. Give the agent the master, caption configuration, and finished image. Ask it to move the caption from the center to the upper edge. | Typeset from the uncaptioned master. Verify that only the placement changes. Check wording, occlusion, and the final image hash. Distinguish the production review from user feedback. |
| Review only | Provide a candidate in which the water obscures the shell and the step cannot be identified. Ask whether the image can be accepted against the first passage. | Inspect the actual detail. Identify the unreadable relationship and give a specific change to viewpoint or composition. Keep the item open for review. |
| Scope of activation | Try “Illustrate the next scene from this passage” and “Copyedit the punctuation in this paragraph.” | The first request calls for continuity checks. The second calls for text editing alone. |

Aspect ratio, palette, and subject belong to the individual case. Judge the actual images, storyboards, prompts, and revisions against their evidence. Counting headings is not a measure of performance.
