---
name: passage-illustrator
description: Create, continue, review, and revise illustrations based on a source text. Use for a single passage, poem, essay, story, or chapter that needs an illustration, a sequence, or artwork captioned with quotations. Also use to storyboard a passage, write image prompts, carry an established design into a new scene, or check existing artwork against the text.
license: MIT
---

# Illustrate a source text

Use the edition or passage the user specifies as the authority for events and quotations. Read the entire passage in scope. Choose the number of illustrations according to the user's request and the density of the material. Select one observable moment for each image. Carry forward the work's established style, character designs, props, and settings. Follow its specifications for aspect ratio, output dimensions, reading direction, lettering within the scene, captions, and series covers.

When asked for illustrations, generate or edit the artwork with the tools available in the host application. Open each result and review it before delivery. If the user asks only for a storyboard, prompts, or a review, deliver that stage. If a required imaging tool is unavailable, identify the outstanding work and supply the materials needed to continue.

## Production sequence

| Stage | Work to complete | Ready to proceed when |
| --- | --- | --- |
| Source text | Extract the passage, assign stable paragraph IDs, and record its provenance. | The selected passage, reading order, and wording match the source. |
| Storyboard | Decide how many images to make. For each, record one moment, the source facts, the artistic choices, and the review criteria. | The sequence reads coherently. The actions and viewpoint fit this point in the story. |
| Reference assets | Locate the relevant character designs, story stages, props, and settings. Identify what each reference establishes. | Key features are explicit, and the actual reference files have been opened and checked. |
| Prompt | Write a detailed, self-contained description that can be drawn as a single image. | The actors, actions, objects, and spatial directions are unambiguous. The chosen composition shows the essential relationships. |
| Master artwork | Review each candidate for fidelity to the text, physical and spatial coherence, and continuity. | Every confirmed error has been corrected and each applicable critical check has passed. Resolve anything too unclear to assess. |
| Finished illustration | Add captions and prepare the cover when requested. Inspect the whole image and the details. | The content is correct, and important relationships remain visible after cropping and typesetting. |
| Delivery | Check the files and archive contents. Update the current review findings. | Visual and technical checks apply to the current files, links work, and retained materials support revision and re-export. |

Record production review, technical verification, and user sign-off separately. A successful generation or export establishes only that the tool completed its operation. Carry out revisions within the authorization already given.

## Working through a project

1. Establish where the authoritative text, storyboard, reference assignments, master artwork, and current review findings live. Follow an existing project's directory conventions. See [Production files and retention](references/materials.md).
2. Locate the source passage, plan the sequence, and define what needs to be visible in each image. Check the established designs, each character's state at this point, and the relevant earlier illustrations. See [Source text and storyboarding](references/source-and-scenes.md) and [Reference assets and continuity](references/continuity.md).
3. Use the prompt-writing standard below and the appropriate [image prompt template](references/prompts.md). Read the completed prompt as a description of one still image before submitting it.
4. Open each candidate and check it against the source text, physical and spatial relationships, and related illustrations. Trace any error back to the storyboard, prompt, reference asset, or artwork. Review the correction before accepting the image. See [Visual review and revision](references/review-and-revision.md).
5. Inspect the finished work, assemble the deliverables, and retain the materials needed for further use. See [Lettering, export, and delivery](references/delivery.md) and [Production files and retention](references/materials.md). The optional [PNG exporter](scripts/export.py) requires Python 3.10+ and Pillow 10.1+. Its inputs and commands are documented in [Export configuration](references/export-format.md).

## Writing image prompts

Write each prompt as a complete illustration brief that makes sense on its own. Describe the people, actions, objects, and setting in as much detail as the composition calls for. Within the tool's input limit, give priority to information that changes what will be drawn. Repeated adjectives add little.

### What to describe

Arrange the description in the following order. Give complex subjects their own paragraphs. Keep each action together with the body parts, objects, and points of contact involved.

| Element | Visual information to specify |
| --- | --- |
| Subject and moment | Type of illustration, place, time, principal event, and the particular instant depicted. Show earlier events through traces that remain visible. |
| Characters | Number, identity, species, features, build, hair or fur, layers of clothing, headwear, equipment, and appearance at this point in the story. Distinguish the principal figures. |
| Action | Orientation of the torso, alignment of shoulders, elbows, wrists, hips, knees, and ankles, what each hand does, and where the feet are placed. Identify who initiates the action, its target, and who responds. |
| Expression and gaze | Brows, eyes, mouth, head angle, and where each person is looking. Give emotions visible form and direct bystanders' reactions toward a specific subject. |
| Object construction | Quantity, silhouette, components and joints, material, color, relative size, orientation, and current condition, including damage where relevant. |
| Contact and weight | How a hand grips or supports an object, how the feet meet the ground, where weight falls, and what bears the load. Make the visible parts of a partly obscured form line up. |
| Setting and space | Foreground, middle ground, background, relative positions, distances, terrain, buildings, entrances, exits, and fixed features. Use one coherent spatial arrangement. |
| Viewpoint and composition | Viewing direction and height, framing, perspective, crop, focal point, depth, separation of silhouettes, and details the viewer must be able to see. |
| Light, color, and technique | Direction of light, tonal and color relationships, linework, application of color, texture, and the treatment of different materials within the same atmosphere. |
| Continuity and output | Features that persist, changes allowed in this image, aspect ratio, lettering within the scene, space for captions, and exclusions specific to this composition. |

Omit elements that do not apply. A distant figure needs only the detail the framing can resolve. If a small feature carries the story, choose a closer view or a different angle. Keep background details consistent with the setting and events. Inventing an extra figure, prop, or landmark can change the reader's understanding of the passage.

### Rules for describing a scene

1. **Assign each action.** In a group scene, identify who acts on whom, which hand acts, and which object it holds. Repeat a name wherever a pronoun could point to two people.
2. **Hold one instant.** Bring bodies, expressions, props, and surroundings into the same moment. Keep future actions in the storyboard. Describe what can already be seen at this stage.
3. **Keep attributes consistent.** Use the same name, material, color, construction, quantity, and condition for a given object throughout the prompt.
4. **Establish orientation.** Distinguish a figure's own left and right from the viewer's. Set the viewpoint before describing direction, occlusion, and perspective.
5. **Describe construction.** Say how parts connect, which surface faces the viewer, and what passes behind what. A request for “correct anatomy” or “natural proportions” leaves those decisions unspecified.
6. **Give scale a visible reference.** Relate size and length to a body, the ground plane, or another object in the scene. Account for distance, tilt, and foreshortening. Pixel lengths across different views can mislead.
7. **Make decisive details legible.** Allow enough space to see an action, a point of contact, or an exact count. If a sleeve, mist, a crop, or a caption hides an unresolved error, correct the underlying image.
8. **Make each prompt self-contained.** Describe the relevant appearance in words. Keep filenames, asset versions, and tracking IDs in the production records.
9. **Match the actual inputs.** Identify each supplied reference image in input order. Specify its purpose, the features it establishes, and what this composition changes. Refer only to images supplied in this request.
10. **Use tool-specific controls correctly.** Describe the composition and aspect ratio in the prompt. Set supported dimensions, masks, and other controls in the tool call. Use negative prompts or weights only where the selected tool supports them.
11. **Consolidate accepted revisions.** Rewrite the affected passages and remove superseded poses, materials, viewpoints, or instructions. Retain one complete, internally consistent prompt for the current artwork.

### Three kinds of image prompt

Use the appropriate [built-in template](references/prompts.md). Replace its fields with the facts, design decisions, and visible relationships for this image. Retain the complete generation prompt. After accepting a local edit, incorporate the resulting visual state into that prompt.

- **First illustration.** Describe the subject, action, space, objects, and technique so the image can be drawn without earlier conversation or project memory.
- **Next illustration in a sequence.** Establish the features and scene state that carry forward, then describe what changes. For a fixed viewpoint, specify fixed positions and contact points. For a change of viewpoint, describe depth, left and right, and occlusion from the new position.
- **Local edit.** Identify the target image, visible defect, edit boundary, intended result, and elements to preserve. Include any connected structures needed to make the correction work.

### Before submitting

Read the prompt as one still image and check it against the passage, storyboard, and current designs.

- Are the identities, counts, targets of actions, ownership of objects, and point in the story correct? Has anything been added without grounds or introduced too early?
- Can the specified hands, feet, poses, expressions, and lines of sight coexist? Does a limb have two incompatible jobs?
- Do the parts, number, connections, orientation, and scale of each object work? Are grips, supports, and occlusions physically plausible?
- Do the viewpoint, framing, crop, and caption space leave the critical structures visible?
- Are continuity requirements expressed as concrete features? Remove obsolete states, ambiguous references, and contradictory sentences.
- Do the actual image inputs, their order, and their stated roles agree? If the host expands prompts, check that it preserves the source facts and established visual relationships.

Correct the storyboard, viewpoint, or wording before generation. Record the resulting decisions in the files that own them. A separate prompt-review report is unnecessary.
