# Image prompt templates

Choose a template for a first illustration, a subsequent illustration, a local edit, or cover artwork. The agent fills the bracketed fields from the passage, storyboard, and current references, then rewrites the result as a fluent, self-contained prompt for the image tool. Omit the figure paragraph in an unpeopled scene and the reference assignments when no images accompany the request. Expand the description where several figures, objects, or spatial relationships need to be distinguished. The user can supply the passage or point to existing project materials.

## First illustration

~~~text
Use Gongbi Narrative Illustration on a Silk-Textured Ground. [Insert the complete fixed art-direction paragraph from SKILL.md.] Carry forward [visible features of the bound character, setting, and prop versions].

Create a [aspect ratio] illustration set in [place and visible surroundings] at [time or lighting condition]. Depict the instant when [one event or state]. The viewer's eye goes first to [focal subject and its visible condition]. [Visible trace] shows that [earlier event] has already taken place.

[Principal figure, identity, and appearance at this stage] stands or sits [position relative to the scene]. Distinguishing features include [build, facial features, hair or fur, clothing layers, and equipment already acquired]. The torso faces [person or object], the head tilts [direction], and the gaze rests on [specific point]. [Brows, mouth, and posture] convey the reaction. [Specific hand or body part] acts on [subject or object] at [point of contact]. The weight rests on [foot or support], making the pose physically possible. [Describe the appearance, actions, responses, and relative positions of the other figures.]

There are [number] [key objects or features]. Their [color, silhouette, materials, components, and joints] are visible. Relative to [visible point of comparison], each is [scale]. At this instant [owner, orientation, and current condition]. [Grip, support, attachment, or relationship to a nearby feature] places it at [location]. From this angle the viewer can distinguish [detail that carries the action or image].

Look from [direction and height] toward [subject], framed as [wide view, medium view, close-up, or other framing]. In the foreground [forms and edges of any occlusion]. In the middle ground [relative placement of figures, props, or landscape features]. In the distance [extension of the setting and its fixed features]. Place the focal point and the edges of the frame so that [required count, body part, or point of contact] remains clearly visible.

Light falls from [direction] across [specific surfaces]. Use [linework, application of color, tonal range, and rendering of materials] to give the scene [established style and atmosphere]. [If the scene contains lettering, give the exact wording, surface, and orientation.] [Reserve the planned area for the selected quotation and editorial title, and describe the background texture to retain. Omit this only for the recorded wordless scope.]
~~~

For landscape, still life, or an image drawn from a poem, spend the detail on shape, depth, light, color, and signs of time passing. Include details required by the text or chosen for this particular design. The [tide-line export fixture](../examples/tide-line/project.json) demonstrates source quoting and export. Its retained color-print artwork and original prompt document an earlier sample. Use the fixed style above for new artwork.

## Next illustration in a sequence

~~~text
Use Gongbi Narrative Illustration on a Silk-Textured Ground. [Insert the complete fixed art-direction paragraph from SKILL.md.] Create the next [aspect ratio] illustration in the series. Depict the instant when [one new action or state].

Use input image [number] for [identity, prop design, setting, or technique]. Carry forward [specific features verified in that image]. Input image [number] establishes [the state of the scene or another reference]. Retain [visible features that still apply].

[Subject's identity, current appearance, and clothing] includes [recognizable features shared across the sequence]. The same [object] can be identified by [silhouette, construction, material, and relative size]. The setting retains [relative positions of fixed features and traces of the preceding action]. In this image [who has moved, who has picked up or put down an object, or how the pose or setting has changed]. Show the result through [current holder, contact point, and position].

The viewer is now at [position and height], with [framing and crop]. From here [relative depth of the subject, fixed objects, and entrances]. [The figure's own left or right side] faces [target]. [Specify what overlaps and what must remain visible.] Focus on [the relationship that gives this scene its purpose], expressed through [expression, gaze, action, or a trace in the setting]. Continue the established [linework, palette, and rendering of materials], with light from [direction at this time of day]. [Space reserved for the selected source quotation and editorial title, or the recorded wordless scope.]
~~~

For a fixed viewpoint, locate fixed structures and contact points. When changing viewpoint, work out left and right, occlusion, and apparent proportions from the new position. Describe identifying features in words even when an earlier illustration is unavailable. Number only the references actually supplied, and limit each reference to its stated role.

## Local edit

~~~text
Edit [input number or other unambiguous identification of the target image]. The visible problem is [defect, subject, and location in the frame]. At this point in the passage the image should show [intended state from the source and storyboard].

Change [specific affected area] to [correct number, shape, direction, or action]. Adjust [connected anatomy, components, occluding edges, or shadows] so that [the grip, joint, weight, perspective, or relationship between lettering and its surface] works. From the existing viewpoint, the viewer should be able to see [observable evidence of the correction]. Confine the edit to [boundary, including the connected features needed for a coherent result].

Preserve [correct facial features, clothing, and pose], [prop identity and fixed elements of the setting], and [original framing, crop, light direction, linework, and surface treatment]. Match the surrounding [contour, texture, tone, or brushwork] at the edge of the edit. [For any additional supplied reference, give its input number and the specific feature to check.]
~~~

A wrong narrative moment, viewpoint, or overall composition calls for a revised storyboard and a new generation prompt. A change to an editorial caption goes through the typesetting configuration. Once a local edit has been accepted, update the complete prompt to describe the revised artwork and inspect the full image, the corrected detail, and the related illustrations.

## Cover artwork

For the first installment of a series, prepare dedicated shared cover artwork and a title template. Later chapters reuse the effective background and template with the current chapter wording. Use this prompt to generate the background in the skill's fixed style, review it, and add titles using the layout tool. A cover uses its own composition and source file.

~~~text
Create dedicated cover artwork for [the series]. Use Gongbi Narrative Illustration on a Silk-Textured Ground. [Insert the complete fixed art-direction paragraph from SKILL.md.] Use [a composition justified by the work as a whole and suitable for reuse across chapters], with [visible features of any bound character, prop, or setting designs]. The principal form is [focal shape and position]. Organize [foreground, middle ground, and distance] to give the cover a clear silhouette and hierarchy at thumbnail size.

Use [palette, linework, application of color, and surface texture] consistently with the story illustrations. Leave [specific region, proportions, and background value] clear for the chapter identifier and original chapter title, arranged in [reading direction]. The background artwork is unlettered so that the verified titles can be typeset on a separate layer. Compose for [final aspect ratio and crop]. For a series template, retain [stable compositional features] across later installments.
~~~

Record the full prompt and reviewed background as cover sources. Typeset the exact chapter identifier and original chapter title according to the existing template. Export and inspect the flattened cover and transparent type layer. For later installments, reuse the effective background and template and change the installment wording.
