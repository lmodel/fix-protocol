


```mermaid
 classDiagram
    class MessageCategory
    click MessageCategory href "../MessageCategory"
      MessageCategory : business_area
        
          
    
        
        
        MessageCategory --> "1" BusinessAreaEnum : business_area
        click BusinessAreaEnum href "../BusinessAreaEnum"
    

        
      MessageCategory : category
        
          
    
        
        
        MessageCategory --> "1" MessageCategoryEnum : category
        click MessageCategoryEnum href "../MessageCategoryEnum"
    

        
      MessageCategory : description
        
      MessageCategory : messages
        
          
    
        
        
        MessageCategory --> "*" Message : messages
        click Message href "../Message"
    

        
      MessageCategory : title
        
      
```
