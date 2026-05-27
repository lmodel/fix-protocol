


```mermaid
 classDiagram
    class UDFTagRange
    click UDFTagRange href "../UDFTagRange"
      UDFTagRange : description
        
      UDFTagRange : high_tag
        
      UDFTagRange : low_tag
        
      UDFTagRange : range_id
        
      UDFTagRange : requires_registration
        
      UDFTagRange : usage
        
          
    
        
        
        UDFTagRange --> "1" UDFTagRangeUsage : usage
        click UDFTagRangeUsage href "../UDFTagRangeUsage"
    

        
      
```
