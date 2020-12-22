# ArcPy-Scripts
A collection of scripts I wrote to improve efficiency in ArcMap/ArcGIS Pro.

**ExportAllLayouts_Pro.py**
This script exports all the layouts that are in an ArcGIS Pro .aprx file to PDF.

**ListLayerDataSources_ArcMap.py**
This script lists the data source for each layer in an MXD’s table of contents.

**ListLayerDataSources_Pro.py**
This script lists the data sources for all layers in all the maps in an ArcGIS Pro .aprx file.

**ReplaceTextWithNewText_SpecificWord_Pro.py**
This script changes element text on all the layouts that are in an ArcGIS Pro .aprx file.
Specifically this searches elements that have a specific word/phrase (in this case, "PROJECT:") and if the element has that, it changes specific text within that.
Put another way, search for an element with a specific word and replace a single thing within it.

**ReplaceTextWithNewText_WholeElement_Pro.py**
This script changes element text on all the layouts that are in an ArcGIS Pro .aprx file.
Specficially, this replaces a whole element text with a new, updated element text.
Put another way, search for exact text of an element and replace whole element text with new text.
