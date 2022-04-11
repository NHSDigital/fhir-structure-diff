# Example output 

The following usage should produce the output below.

```shell
python fhir_structure_diff.py ./tests/data/CareConnect-AllergyIntolerance-1.json ./tests/data/CareConnect-GPC-AllergyIntolerance-1.json
```

# FHIR Profile Diff  
**Base profile:** AllergyIntolerance
|Lefthand Profile|Version|
|----|----|
|CareConnect-AllergyIntolerance-1|3.0.1|

|Righthand Profile|Version|
|----|----|
|CareConnect-GPC-AllergyIntolerance-1|3.0.1|
---
# Element level diff  
**Profiles:**
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
**Diff:**
```diff  
+AllergyIntolerance.meta.profile  
 AllergyIntolerance.extension  
 AllergyIntolerance.extension:encounter  
 AllergyIntolerance.extension:allergyEnd  
 AllergyIntolerance.extension:evidence  
+AllergyIntolerance.identifier  
 AllergyIntolerance.identifier.system  
 AllergyIntolerance.identifier.value  
-AllergyIntolerance.identifier.assigner  
+AllergyIntolerance.clinicalStatus  
 AllergyIntolerance.verificationStatus  
-AllergyIntolerance.code.coding  
-AllergyIntolerance.code.coding:snomedCT  
-AllergyIntolerance.code.coding:snomedCT.extension  
-AllergyIntolerance.code.coding:snomedCT.extension:snomedCTDescriptionID  
-AllergyIntolerance.code.coding:snomedCT.system  
-AllergyIntolerance.code.coding:snomedCT.code  
-AllergyIntolerance.code.coding:snomedCT.display  
+AllergyIntolerance.category  
+AllergyIntolerance.code  
+AllergyIntolerance.code.coding.extension  
+AllergyIntolerance.code.coding.extension:snomedCTDescriptionID  
+AllergyIntolerance.code.coding.system  
+AllergyIntolerance.code.coding.version  
+AllergyIntolerance.code.coding.code  
 AllergyIntolerance.patient  
 AllergyIntolerance.onset[x]  
 AllergyIntolerance.assertedDate  
 AllergyIntolerance.recorder  
 AllergyIntolerance.asserter  
+AllergyIntolerance.note  
 AllergyIntolerance.note.author[x]  
 AllergyIntolerance.reaction.substance.coding  
 AllergyIntolerance.reaction.substance.coding:snomedCT  
 AllergyIntolerance.reaction.substance.coding:snomedCT.extension  
 AllergyIntolerance.reaction.substance.coding:snomedCT.extension:snomedCTDescriptionID  
 AllergyIntolerance.reaction.substance.coding:snomedCT.system  
+AllergyIntolerance.reaction.substance.coding:snomedCT.version  
 AllergyIntolerance.reaction.substance.coding:snomedCT.code  
-AllergyIntolerance.reaction.substance.coding:snomedCT.display  
 AllergyIntolerance.reaction.manifestation  
 AllergyIntolerance.reaction.manifestation.coding  
 AllergyIntolerance.reaction.manifestation.coding:snomedCT  
 AllergyIntolerance.reaction.manifestation.coding:snomedCT.extension  
 AllergyIntolerance.reaction.manifestation.coding:snomedCT.extension:snomedCTDescriptionID  
 AllergyIntolerance.reaction.manifestation.coding:snomedCT.system  
+AllergyIntolerance.reaction.manifestation.coding:snomedCT.version  
 AllergyIntolerance.reaction.manifestation.coding:snomedCT.code  
-AllergyIntolerance.reaction.manifestation.coding:snomedCT.display  
 AllergyIntolerance.reaction.severity  
 AllergyIntolerance.reaction.exposureRoute  
 AllergyIntolerance.reaction.exposureRoute.coding  
 AllergyIntolerance.reaction.exposureRoute.coding:snomedCT  
 AllergyIntolerance.reaction.exposureRoute.coding:snomedCT.extension  
 AllergyIntolerance.reaction.exposureRoute.coding:snomedCT.extension:snomedCTDescriptionID  
 AllergyIntolerance.reaction.exposureRoute.coding:snomedCT.system  
+AllergyIntolerance.reaction.exposureRoute.coding:snomedCT.version  
 AllergyIntolerance.reaction.exposureRoute.coding:snomedCT.code  
-AllergyIntolerance.reaction.exposureRoute.coding:snomedCT.display  
 AllergyIntolerance.reaction.note.author[x]  

```
---
# Component level diff  

## Element: *AllergyIntolerance.extension*  

### Component: *slicing*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Match|Match|

#### Match  
```json  
{
  "discriminator": [
    {
      "path": "url",
      "type": "value"
    }
  ],
  "rules": "open"
}  
```  



#### Base  
```json
{
  "description": "Extensions are always sliced by (at least) url",
  "discriminator": [
    {
      "path": "url",
      "type": "value"
    }
  ],
  "rules": "open"
}
```  



## Element: *AllergyIntolerance.extension:encounter*  

### Component: *mustSupport*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Not defined|True|



#### Base  
"mustSupport" is not defined in the base element definition.  



## Element: *AllergyIntolerance.extension:allergyEnd*  

### Component: *mustSupport*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Not defined|True|



#### Base  
"mustSupport" is not defined in the base element definition.  



## Element: *AllergyIntolerance.extension:evidence*  

### Component: *type*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|See diff|See diff|


#### Diff  
```diff  
 [  
   {  
     "code": "Extension",  
-    "profile": "https://fhir.hl7.org.uk/STU3/StructureDefinition/Extension-CareConnect-Evidence-1"  
+    "profile": "https://fhir.nhs.uk/STU3/StructureDefinition/Extension-CareConnect-GPC-Evidence-1"  
   }  
 ]  
  
```  


#### Base  
```json
[
  {
    "code": "Extension"
  }
]
```  



## Element: *AllergyIntolerance.identifier.system*  

### Component: *min*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Match. "min" == 1|Match. "min" == 1|



#### Base  
"min" == 0  



## Element: *AllergyIntolerance.identifier.value*  

### Component: *min*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Match. "min" == 1|Match. "min" == 1|



#### Base  
"min" == 0  



## Element: *AllergyIntolerance.verificationStatus*  

### Component: *fixedCode*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Not defined|unconfirmed|



#### Base  
"fixedCode" is not defined in the base element definition.  



## Element: *AllergyIntolerance.patient*  

### Component: *type*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|See diff|See diff|


#### Diff  
```diff  
 [  
   {  
     "code": "Reference",  
-    "targetProfile": "https://fhir.hl7.org.uk/STU3/StructureDefinition/CareConnect-Patient-1"  
+    "targetProfile": "https://fhir.nhs.uk/STU3/StructureDefinition/CareConnect-GPC-Patient-1"  
   }  
 ]  
  
```  


#### Base  
```json
[
  {
    "code": "Reference",
    "targetProfile": "http://hl7.org/fhir/StructureDefinition/Patient"
  }
]
```  



## Element: *AllergyIntolerance.onset[x]*  

### Component: *mustSupport*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Match. "mustSupport" == True|Match. "mustSupport" == True|



#### Base  
"mustSupport" is not defined in the base element definition.  



## Element: *AllergyIntolerance.assertedDate*  

### Component: *min*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Match. "min" == 1|Match. "min" == 1|



#### Base  
"min" == 0  



## Element: *AllergyIntolerance.recorder*  

### Component: *min*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Not defined|1|



#### Base  
"min" == 0  



## Element: *AllergyIntolerance.asserter*  

### Component: *mustSupport*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Not defined|True|



#### Base  
"mustSupport" is not defined in the base element definition.  



## Element: *AllergyIntolerance.note.author[x]*  

### Component: *type*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|See diff|See diff|


#### Diff  
```diff  
 [  
   {  
     "code": "Reference",  
     "targetProfile": "http://hl7.org/fhir/StructureDefinition/RelatedPerson"  
   },  
   {  
     "code": "string"  
   },  
   {  
     "code": "Reference",  
-    "targetProfile": "https://fhir.hl7.org.uk/STU3/StructureDefinition/CareConnect-Patient-1"  
+    "targetProfile": "https://fhir.nhs.uk/STU3/StructureDefinition/CareConnect-GPC-Patient-1"  
   },  
   {  
     "code": "Reference",  
-    "targetProfile": "https://fhir.hl7.org.uk/STU3/StructureDefinition/CareConnect-Practitioner-1"  
+    "targetProfile": "https://fhir.nhs.uk/STU3/StructureDefinition/CareConnect-GPC-Practitioner-1"  
   }  
 ]  
  
```  


#### Base  
```json
[
  {
    "code": "Reference",
    "targetProfile": "http://hl7.org/fhir/StructureDefinition/Practitioner"
  },
  {
    "code": "Reference",
    "targetProfile": "http://hl7.org/fhir/StructureDefinition/Patient"
  },
  {
    "code": "Reference",
    "targetProfile": "http://hl7.org/fhir/StructureDefinition/RelatedPerson"
  },
  {
    "code": "string"
  }
]
```  



## Element: *AllergyIntolerance.reaction.substance.coding*  

### Component: *slicing*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Match|Match|

#### Match  
```json  
{
  "discriminator": [
    {
      "path": "system",
      "type": "value"
    }
  ],
  "ordered": false,
  "rules": "open"
}  
```  



#### Base  
"slicing" is not defined in the base element definition.  



## Element: *AllergyIntolerance.reaction.substance.coding:snomedCT*  

### Component: *max*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Match. "max" == 1|Match. "max" == 1|



#### Base  
"max" == *  



## Element: *AllergyIntolerance.reaction.substance.coding:snomedCT.extension*  

### Component: *slicing*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Match|Match|

#### Match  
```json  
{
  "discriminator": [
    {
      "path": "url",
      "type": "value"
    }
  ],
  "rules": "open"
}  
```  



#### Base  
```json
{
  "description": "Extensions are always sliced by (at least) url",
  "discriminator": [
    {
      "path": "url",
      "type": "value"
    }
  ],
  "rules": "open"
}
```  



## Element: *AllergyIntolerance.reaction.substance.coding:snomedCT.extension:snomedCTDescriptionID*  

### Component: *type*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|See diff|See diff|


#### Diff  
```diff  
 [  
   {  
     "code": "Extension",  
-    "profile": "https://fhir.hl7.org.uk/STU3/StructureDefinition/Extension-coding-sctdescid"  
+    "profile": "https://fhir.nhs.uk/STU3/StructureDefinition/Extension-coding-sctdescid"  
   }  
 ]  
  
```  


#### Base  
```json
[
  {
    "code": "Extension"
  }
]
```  



## Element: *AllergyIntolerance.reaction.substance.coding:snomedCT.system*  

### Component: *fixedUri*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Match. "fixedUri" == http://snomed.info/sct|Match. "fixedUri" == http://snomed.info/sct|



#### Base  
"fixedUri" is not defined in the base element definition.  



## Element: *AllergyIntolerance.reaction.substance.coding:snomedCT.code*  

### Component: *min*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Match. "min" == 1|Match. "min" == 1|



#### Base  
"min" == 0  



## Element: *AllergyIntolerance.reaction.manifestation*  

### Component: *binding*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Match|Match|

#### Match  
```json  
{
  "extension": [
    {
      "url": "http://hl7.org/fhir/StructureDefinition/elementdefinition-bindingName",
      "valueString": "Manifestation"
    }
  ],
  "strength": "extensible",
  "valueSetReference": {
    "reference": "https://fhir.hl7.org.uk/STU3/ValueSet/CareConnect-AllergyManifestation-1"
  }
}  
```  



#### Base  
```json
{
  "description": "Clinical symptoms and/or signs that are observed or associated with an Adverse Reaction Event.",
  "extension": [
    {
      "url": "http://hl7.org/fhir/StructureDefinition/elementdefinition-bindingName",
      "valueString": "Manifestation"
    }
  ],
  "strength": "example",
  "valueSetReference": {
    "reference": "http://hl7.org/fhir/ValueSet/clinical-findings"
  }
}
```  



## Element: *AllergyIntolerance.reaction.manifestation.coding*  

### Component: *slicing*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Match|Match|

#### Match  
```json  
{
  "discriminator": [
    {
      "path": "system",
      "type": "value"
    }
  ],
  "ordered": false,
  "rules": "open"
}  
```  



#### Base  
"slicing" is not defined in the base element definition.  



## Element: *AllergyIntolerance.reaction.manifestation.coding:snomedCT*  

### Component: *max*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Match. "max" == 1|Match. "max" == 1|



#### Base  
"max" == *  



## Element: *AllergyIntolerance.reaction.manifestation.coding:snomedCT.extension*  

### Component: *slicing*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Match|Match|

#### Match  
```json  
{
  "discriminator": [
    {
      "path": "url",
      "type": "value"
    }
  ],
  "rules": "open"
}  
```  



#### Base  
```json
{
  "description": "Extensions are always sliced by (at least) url",
  "discriminator": [
    {
      "path": "url",
      "type": "value"
    }
  ],
  "rules": "open"
}
```  



## Element: *AllergyIntolerance.reaction.manifestation.coding:snomedCT.extension:snomedCTDescriptionID*  

### Component: *type*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|See diff|See diff|


#### Diff  
```diff  
 [  
   {  
     "code": "Extension",  
-    "profile": "https://fhir.hl7.org.uk/STU3/StructureDefinition/Extension-coding-sctdescid"  
+    "profile": "https://fhir.nhs.uk/STU3/StructureDefinition/Extension-coding-sctdescid"  
   }  
 ]  
  
```  


#### Base  
```json
[
  {
    "code": "Extension"
  }
]
```  



## Element: *AllergyIntolerance.reaction.manifestation.coding:snomedCT.system*  

### Component: *fixedUri*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Match. "fixedUri" == http://snomed.info/sct|Match. "fixedUri" == http://snomed.info/sct|



#### Base  
"fixedUri" is not defined in the base element definition.  



## Element: *AllergyIntolerance.reaction.manifestation.coding:snomedCT.code*  

### Component: *min*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Match. "min" == 1|Match. "min" == 1|



#### Base  
"min" == 0  



## Element: *AllergyIntolerance.reaction.severity*  

### Component: *mustSupport*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Not defined|True|



#### Base  
"mustSupport" is not defined in the base element definition.  



## Element: *AllergyIntolerance.reaction.exposureRoute*  

### Component: *binding*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|See diff|See diff|


#### Diff  
```diff  
 {  
   "extension": [  
     {  
       "url": "http://hl7.org/fhir/StructureDefinition/elementdefinition-bindingName",  
       "valueString": "RouteOfAdministration"  
     }  
   ],  
   "strength": "example",  
   "valueSetReference": {  
-    "reference": "https://fhir.hl7.org.uk/STU3/ValueSet/CareConnect-AllergyExposureRoute-1"  
+    "reference": "https://fhir.nhs.uk/STU3/ValueSet/CareConnect-AllergyExposureRoute-1"  
   }  
 }  
  
```  


#### Base  
```json
{
  "description": "A coded concept describing the route or physiological path of administration of a therapeutic agent into or onto the body of a subject.",
  "extension": [
    {
      "url": "http://hl7.org/fhir/StructureDefinition/elementdefinition-bindingName",
      "valueString": "RouteOfAdministration"
    }
  ],
  "strength": "example",
  "valueSetReference": {
    "reference": "http://hl7.org/fhir/ValueSet/route-codes"
  }
}
```  



## Element: *AllergyIntolerance.reaction.exposureRoute.coding*  

### Component: *slicing*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Match|Match|

#### Match  
```json  
{
  "discriminator": [
    {
      "path": "system",
      "type": "value"
    }
  ],
  "ordered": false,
  "rules": "open"
}  
```  



#### Base  
"slicing" is not defined in the base element definition.  



## Element: *AllergyIntolerance.reaction.exposureRoute.coding:snomedCT*  

### Component: *max*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Match. "max" == 1|Match. "max" == 1|



#### Base  
"max" == *  



## Element: *AllergyIntolerance.reaction.exposureRoute.coding:snomedCT.extension*  

### Component: *slicing*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Match|Match|

#### Match  
```json  
{
  "discriminator": [
    {
      "path": "url",
      "type": "value"
    }
  ],
  "rules": "open"
}  
```  



#### Base  
```json
{
  "description": "Extensions are always sliced by (at least) url",
  "discriminator": [
    {
      "path": "url",
      "type": "value"
    }
  ],
  "rules": "open"
}
```  



## Element: *AllergyIntolerance.reaction.exposureRoute.coding:snomedCT.extension:snomedCTDescriptionID*  

### Component: *type*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|See diff|See diff|


#### Diff  
```diff  
 [  
   {  
     "code": "Extension",  
-    "profile": "https://fhir.hl7.org.uk/STU3/StructureDefinition/Extension-coding-sctdescid"  
+    "profile": "https://fhir.nhs.uk/STU3/StructureDefinition/Extension-coding-sctdescid"  
   }  
 ]  
  
```  


#### Base  
```json
[
  {
    "code": "Extension"
  }
]
```  



## Element: *AllergyIntolerance.reaction.exposureRoute.coding:snomedCT.system*  

### Component: *fixedUri*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Match. "fixedUri" == http://snomed.info/sct|Match. "fixedUri" == http://snomed.info/sct|



#### Base  
"fixedUri" is not defined in the base element definition.  



## Element: *AllergyIntolerance.reaction.exposureRoute.coding:snomedCT.code*  

### Component: *min*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Match. "min" == 1|Match. "min" == 1|



#### Base  
"min" == 0  



## Element: *AllergyIntolerance.reaction.note.author[x]*  

### Component: *type*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|See diff|See diff|


#### Diff  
```diff  
 [  
   {  
     "code": "Reference",  
     "targetProfile": "http://hl7.org/fhir/StructureDefinition/RelatedPerson"  
   },  
   {  
     "code": "string"  
   },  
   {  
     "code": "Reference",  
-    "targetProfile": "https://fhir.hl7.org.uk/STU3/StructureDefinition/CareConnect-Patient-1"  
+    "targetProfile": "https://fhir.nhs.uk/STU3/StructureDefinition/CareConnect-GPC-Patient-1"  
   },  
   {  
     "code": "Reference",  
-    "targetProfile": "https://fhir.hl7.org.uk/STU3/StructureDefinition/CareConnect-Practitioner-1"  
+    "targetProfile": "https://fhir.nhs.uk/STU3/StructureDefinition/CareConnect-GPC-Practitioner-1"  
   }  
 ]  
  
```  


#### Base  
```json
[
  {
    "code": "Reference",
    "targetProfile": "http://hl7.org/fhir/StructureDefinition/Practitioner"
  },
  {
    "code": "Reference",
    "targetProfile": "http://hl7.org/fhir/StructureDefinition/Patient"
  },
  {
    "code": "Reference",
    "targetProfile": "http://hl7.org/fhir/StructureDefinition/RelatedPerson"
  },
  {
    "code": "string"
  }
]
```  



## Element: *AllergyIntolerance.identifier.assigner*  

### Component: *type*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Nothing to diff, value below|Not defined|


#### Diff  
```diff  
[
  {
    "code": "Reference",
    "targetProfile": "https://fhir.hl7.org.uk/STU3/StructureDefinition/CareConnect-Organization-1"
  }
]  
```  


#### Base  
```json
[
  {
    "code": "Reference",
    "targetProfile": "http://hl7.org/fhir/StructureDefinition/Organization"
  }
]
```  



## Element: *AllergyIntolerance.code.coding*  

### Component: *slicing*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Nothing to diff, value below|Not defined|


#### Diff  
```diff  
{
  "discriminator": [
    {
      "path": "system",
      "type": "value"
    }
  ],
  "rules": "open"
}  
```  


#### Base  
"slicing" is not defined in the base element definition.  



## Element: *AllergyIntolerance.code.coding:snomedCT*  

### Component: *binding*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Nothing to diff, value below|Not defined|


#### Diff  
```diff  
{
  "description": "A code from the SNOMED Clinical Terminology UK or a code from the v3 Code System NullFlavor specifying why a valid value is not present.",
  "strength": "example",
  "valueSetReference": {
    "reference": "https://fhir.hl7.org.uk/STU3/ValueSet/CareConnect-AllergyCode-1"
  }
}  
```  


#### Base  
"binding" is not defined in the base element definition.  



## Element: *AllergyIntolerance.code.coding:snomedCT.extension*  

### Component: *slicing*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Nothing to diff, value below|Not defined|


#### Diff  
```diff  
{
  "discriminator": [
    {
      "path": "url",
      "type": "value"
    }
  ],
  "rules": "open"
}  
```  


#### Base  
```json
{
  "description": "Extensions are always sliced by (at least) url",
  "discriminator": [
    {
      "path": "url",
      "type": "value"
    }
  ],
  "rules": "open"
}
```  



## Element: *AllergyIntolerance.code.coding:snomedCT.extension:snomedCTDescriptionID*  

### Component: *type*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Nothing to diff, value below|Not defined|


#### Diff  
```diff  
[
  {
    "code": "Extension",
    "profile": "https://fhir.hl7.org.uk/STU3/StructureDefinition/Extension-coding-sctdescid"
  }
]  
```  


#### Base  
```json
[
  {
    "code": "Extension"
  }
]
```  



## Element: *AllergyIntolerance.code.coding:snomedCT.system*  

### Component: *min*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|1|Not defined|



#### Base  
"min" == 0  



## Element: *AllergyIntolerance.code.coding:snomedCT.code*  

### Component: *min*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|1|Not defined|



#### Base  
"min" == 0  



## Element: *AllergyIntolerance.code.coding:snomedCT.display*  

### Component: *min*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|1|Not defined|



#### Base  
"min" == 0  



## Element: *AllergyIntolerance.reaction.substance.coding:snomedCT.display*  

### Component: *min*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|1|Not defined|



#### Base  
"min" == 0  



## Element: *AllergyIntolerance.reaction.manifestation.coding:snomedCT.display*  

### Component: *min*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|1|Not defined|



#### Base  
"min" == 0  



## Element: *AllergyIntolerance.reaction.exposureRoute.coding:snomedCT.display*  

### Component: *min*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|1|Not defined|



#### Base  
"min" == 0  



## Element: *AllergyIntolerance.meta.profile*  

### Component: *min*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Not defined|1|



#### Base  
"min" == 0  



## Element: *AllergyIntolerance.identifier*  

### Component: *min*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Not defined|1|



#### Base  
"min" == 0  



## Element: *AllergyIntolerance.clinicalStatus*  

### Component: *min*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Not defined|1|



#### Base  
"min" == 0  



## Element: *AllergyIntolerance.category*  

### Component: *min*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Not defined|1|



#### Base  
"min" == 0  



## Element: *AllergyIntolerance.code*  

### Component: *binding*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Not defined|Nothing to diff, value below|


#### Diff  
```diff  
{
  "extension": [
    {
      "url": "http://hl7.org/fhir/StructureDefinition/elementdefinition-bindingName",
      "valueString": "AllergyIntoleranceCode"
    }
  ],
  "strength": "example",
  "valueSetReference": {
    "reference": "https://fhir.nhs.uk/STU3/ValueSet/CareConnect-AllergyCode-1"
  }
}  
```  


#### Base  
```json
{
  "description": "Type of the substance/product, allergy or intolerance condition, or negation/exclusion codes for reporting no known allergies.",
  "extension": [
    {
      "url": "http://hl7.org/fhir/StructureDefinition/elementdefinition-bindingName",
      "valueString": "AllergyIntoleranceCode"
    }
  ],
  "strength": "example",
  "valueSetReference": {
    "reference": "http://hl7.org/fhir/ValueSet/allergyintolerance-code"
  }
}
```  



## Element: *AllergyIntolerance.code.coding.extension*  

### Component: *slicing*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Not defined|Nothing to diff, value below|


#### Diff  
```diff  
{
  "discriminator": [
    {
      "path": "url",
      "type": "value"
    }
  ],
  "rules": "open"
}  
```  


#### Base  
```json
{
  "description": "Extensions are always sliced by (at least) url",
  "discriminator": [
    {
      "path": "url",
      "type": "value"
    }
  ],
  "rules": "open"
}
```  



## Element: *AllergyIntolerance.code.coding.extension:snomedCTDescriptionID*  

### Component: *type*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Not defined|Nothing to diff, value below|


#### Diff  
```diff  
[
  {
    "code": "Extension",
    "profile": "https://fhir.nhs.uk/STU3/StructureDefinition/Extension-coding-sctdescid"
  }
]  
```  


#### Base  
```json
[
  {
    "code": "Extension"
  }
]
```  



## Element: *AllergyIntolerance.code.coding.system*  

### Component: *min*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Not defined|1|



#### Base  
"min" == 0  



## Element: *AllergyIntolerance.code.coding.version*  

### Component: *max*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Not defined|0|



#### Base  
"max" == 1  



## Element: *AllergyIntolerance.code.coding.code*  

### Component: *min*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Not defined|1|



#### Base  
"min" == 0  



## Element: *AllergyIntolerance.note*  

### Component: *mustSupport*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Not defined|True|



#### Base  
"mustSupport" is not defined in the base element definition.  



## Element: *AllergyIntolerance.reaction.substance.coding:snomedCT.version*  

### Component: *max*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Not defined|0|



#### Base  
"max" == 1  



## Element: *AllergyIntolerance.reaction.manifestation.coding:snomedCT.version*  

### Component: *max*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Not defined|0|



#### Base  
"max" == 1  



## Element: *AllergyIntolerance.reaction.exposureRoute.coding:snomedCT.version*  

### Component: *max*  
|CareConnect-AllergyIntolerance-1|CareConnect-GPC-AllergyIntolerance-1|
|----|----|
|Not defined|0|



#### Base  
"max" == 1  


