


```mermaid
 classDiagram
    class TradeAppendixSection
    click TradeAppendixSection href "../TradeAppendixSection"
      TradeAppendixSection : components
        
          
    
        
        
        TradeAppendixSection --> "*" TradeComponentDetail : components
        click TradeComponentDetail href "../TradeComponentDetail"
    

        
      TradeAppendixSection : description
        
      TradeAppendixSection : messages
        
          
    
        
        
        TradeAppendixSection --> "*" TradeMessageDetail : messages
        click TradeMessageDetail href "../TradeMessageDetail"
    

        
      TradeAppendixSection : title
        
      TradeAppendixSection : trade_appendix_category
        
      
```
