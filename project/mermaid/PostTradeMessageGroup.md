


```mermaid
 classDiagram
    class PostTradeMessageGroup
    click PostTradeMessageGroup href "../PostTradeMessageGroup"
      PostTradeMessageGroup : group_title
        
      PostTradeMessageGroup : messages
        
          
    
        
        
        PostTradeMessageGroup --> "1..*" PostTradeMessageDetail : messages
        click PostTradeMessageDetail href "../PostTradeMessageDetail"
    

        
      
```
