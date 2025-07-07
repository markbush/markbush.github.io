What is a Panorama?
###################

:date: 2025-07-06 17:15
:summary: An investigation into what is required for Apple products to recognise an image as a panorama.

A question which I have seen posted on many sites and forums is how to get Apple's Photos app to recognise an image as a panorama.

.. image:: {static}/images/screenshots/photos-media-types.png
  :alt: List of media types recognised by the Photos app.
  :class: left, small

There are a number of different media types which the Photos app automatically recognises.  Many of these are determined by metadata in the image file.  For example, a "User Comment" element in the metadata with a value of "Screenshot" determines if the item is listed as a screenshot.  For panoramas, it is based on the height of the image in pixels and the aspect ratio.

The aspect ratio needs to be at least 2:1 (width:height).  Even 1 pixel over this ratio will do.  This is probably because equirectangular projection, with a ratio of exactly 2:1, is the most common format for 360x180 images (spherical images covering all views around a point).  By selecting images that have any greater ratio, these equirectangular images are not incorrectly classified.

Given that the aspect ratio of an image is over 2:1, the height must also be over 800 pixels to be counted as a panorama.  It is not clear why this is the case, but may be another choice that prevents false positives.  This is because it is common, especially when referring to web or application elements, to end up with long, thin crops of parts of a screen.  It would not be reasonable to consider these to be fully fledged panoramas!  Although the minimum height of 801 pixels would actually be quite poor quality when expanded, it is perfectly good for web banners and would probably ensure that panoramas taken with old cameras, or scanned at a lower quality from photos, are likely to get included.

.. class:: clear

In summary, then, to ensure that an image is recognised as a panorama when imported into the Apple Photos app, make sure that it is a minimum of 801 pixels high and that the width is at least 1 pixel more than twice the height.

I would not be surprised if similar criteria are used for other platforms and applications, however I don't have access to any myself to check.
