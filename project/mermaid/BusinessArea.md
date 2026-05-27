


```mermaid
 classDiagram
    class BusinessArea
    click BusinessArea href "../BusinessArea"
      BusinessArea : area
        
          
    
        
        
        BusinessArea --> "1" BusinessAreaEnum : area
        click BusinessAreaEnum href "../BusinessAreaEnum"
    

        
      BusinessArea : categories
        
          
    
        
        
        BusinessArea --> "*" MessageCategory : categories
        click MessageCategory href "../MessageCategory"
    

        
      BusinessArea : description
        
      BusinessArea : title
        
      
```
