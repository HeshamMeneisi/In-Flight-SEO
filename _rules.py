# Transformation rules

# This can also be parsed from JSON on the source S3
rules = \
[{
  "pattern": "/about",
  "transformations": [{
    "name": "inject_meta_field",
    "params": {"field": "<meta name=description value=\"This is the about section!\"/>"}
   },
   {
    "name": "replace_meta_value",
    "params":{"id_attrib": "property",
    "id_value": "og:title",
    "new_value": "About"}
   }]
 },
 {
  "pattern": "/services",
  "transformations": [{
   "name": "replace_meta_value",
   "params": {"id_attrib": "property",
   "id_value": "og:title",
   "new_value": "Services"}
  }]
 }]
