


```mermaid
 classDiagram
    class TradeMessageGroup
    click TradeMessageGroup href "../TradeMessageGroup"
      TradeMessageGroup : description
        
      TradeMessageGroup : messages
        
          
    
        
        
        TradeMessageGroup --> "1..*" TradeMessageDetail : messages
        click TradeMessageDetail href "../TradeMessageDetail"
    

        
      TradeMessageGroup : trade_group_title
        
      TradeMessageGroup : trade_ord_status_precedence_entries
        
          
    
        
        
        TradeMessageGroup --> "*" TradeOrdStatusPrecedenceEntry : trade_ord_status_precedence_entries
        click TradeOrdStatusPrecedenceEntry href "../TradeOrdStatusPrecedenceEntry"
    

        
      
```
