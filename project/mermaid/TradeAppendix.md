


```mermaid
 classDiagram
    class TradeAppendix
    click TradeAppendix href "../TradeAppendix"
      TradeAppendix : description
        
      TradeAppendix : published_version
        
      TradeAppendix : publisher
        
      TradeAppendix : title
        
      TradeAppendix : trade_appendix_sections
        
          
    
        
        
        TradeAppendix --> "*" TradeAppendixSection : trade_appendix_sections
        click TradeAppendixSection href "../TradeAppendixSection"
    

        
      
```
