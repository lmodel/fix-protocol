


```mermaid
 classDiagram
    class PreTradeBusinessArea
    click PreTradeBusinessArea href "../PreTradeBusinessArea"
      PreTradeBusinessArea : area
        
          
    
        
        
        PreTradeBusinessArea --> "1" BusinessAreaEnum : area
        click BusinessAreaEnum href "../BusinessAreaEnum"
    

        
      PreTradeBusinessArea : category_sections
        
          
    
        
        
        PreTradeBusinessArea --> "*" PreTradeCategorySection : category_sections
        click PreTradeCategorySection href "../PreTradeCategorySection"
    

        
      PreTradeBusinessArea : common_component_details
        
          
    
        
        
        PreTradeBusinessArea --> "*" CommonComponentDetail : common_component_details
        click CommonComponentDetail href "../CommonComponentDetail"
    

        
      PreTradeBusinessArea : common_components
        
          
    
        
        
        PreTradeBusinessArea --> "*" PreTradeCommonComponentName : common_components
        click PreTradeCommonComponentName href "../PreTradeCommonComponentName"
    

        
      PreTradeBusinessArea : components
        
          
    
        
        
        PreTradeBusinessArea --> "*" PreTradeComponentEntry : components
        click PreTradeComponentEntry href "../PreTradeComponentEntry"
    

        
      PreTradeBusinessArea : components_overview_note
        
      PreTradeBusinessArea : diagram_conventions
        
      PreTradeBusinessArea : footnotes
        
          
    
        
        
        PreTradeBusinessArea --> "*" ComponentTableFootnote : footnotes
        click ComponentTableFootnote href "../ComponentTableFootnote"
    

        
      PreTradeBusinessArea : introduction
        
      PreTradeBusinessArea : messages
        
          
    
        
        
        PreTradeBusinessArea --> "*" PreTradeMessageEntry : messages
        click PreTradeMessageEntry href "../PreTradeMessageEntry"
    

        
      PreTradeBusinessArea : messages_overview_note
        
      PreTradeBusinessArea : published_version
        
      PreTradeBusinessArea : publisher
        
      PreTradeBusinessArea : referenced_global_components
        
          
    
        
        
        PreTradeBusinessArea --> "*" GlobalComponent : referenced_global_components
        click GlobalComponent href "../GlobalComponent"
    

        
      PreTradeBusinessArea : title
        
      
```
