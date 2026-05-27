


```mermaid
 classDiagram
    class ExtensionPack
    click ExtensionPack href "../ExtensionPack"
      ExtensionPack : applies_to_fixml_only
        
      ExtensionPack : applies_to_session_layer_only
        
      ExtensionPack : enhancement_summary
        
      ExtensionPack : number
        
      ExtensionPack : size
        
          
    
        
        
        ExtensionPack --> "0..1" ExtensionPackSize : size
        click ExtensionPackSize href "../ExtensionPackSize"
    

        
      ExtensionPack : title
        
      
```
