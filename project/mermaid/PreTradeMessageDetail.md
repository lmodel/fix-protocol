


```mermaid
 classDiagram
    class PreTradeMessageDetail
    click PreTradeMessageDetail href "../PreTradeMessageDetail"
      PreTradeMessageDetail : description
        
      PreTradeMessageDetail : layout_url
        
      PreTradeMessageDetail : message_name
        
      PreTradeMessageDetail : msg_type
        
      PreTradeMessageDetail : pre_layout_rows
        
          
    
        
        
        PreTradeMessageDetail --> "*" PreTradeLayoutRow : pre_layout_rows
        click PreTradeLayoutRow href "../PreTradeLayoutRow"
    

        
      
```
