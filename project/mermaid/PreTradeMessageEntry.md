


```mermaid
 classDiagram
    class PreTradeMessageEntry
    click PreTradeMessageEntry href "../PreTradeMessageEntry"
      PreTradeMessageEntry : category
        
          
    
        
        
        PreTradeMessageEntry --> "1" PreTradeCategoryEnum : category
        click PreTradeCategoryEnum href "../PreTradeCategoryEnum"
    

        
      PreTradeMessageEntry : message_name
        
      PreTradeMessageEntry : msg_type
        
      
```
