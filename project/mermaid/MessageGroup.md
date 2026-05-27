


```mermaid
 classDiagram
    class MessageGroup
    click MessageGroup href "../MessageGroup"
      MessageGroup : description
        
      MessageGroup : group_title
        
      MessageGroup : messages
        
          
    
        
        
        MessageGroup --> "1..*" PreTradeMessageDetail : messages
        click PreTradeMessageDetail href "../PreTradeMessageDetail"
    

        
      
```
