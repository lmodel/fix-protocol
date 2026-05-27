


```mermaid
 classDiagram
    class TradeBusinessArea
    click TradeBusinessArea href "../TradeBusinessArea"
      TradeBusinessArea : components
        
          
    
        
        
        TradeBusinessArea --> "*" TradeComponentEntry : components
        click TradeComponentEntry href "../TradeComponentEntry"
    

        
      TradeBusinessArea : messages
        
          
    
        
        
        TradeBusinessArea --> "*" TradeMessageEntry : messages
        click TradeMessageEntry href "../TradeMessageEntry"
    

        
      TradeBusinessArea : published_version
        
      TradeBusinessArea : publisher
        
      TradeBusinessArea : referenced_global_components
        
          
    
        
        
        TradeBusinessArea --> "*" GlobalComponent : referenced_global_components
        click GlobalComponent href "../GlobalComponent"
    

        
      TradeBusinessArea : title
        
      TradeBusinessArea : trade_area
        
          
    
        
        
        TradeBusinessArea --> "1" BusinessAreaEnum : trade_area
        click BusinessAreaEnum href "../BusinessAreaEnum"
    

        
      TradeBusinessArea : trade_category_sections
        
          
    
        
        
        TradeBusinessArea --> "*" TradeCategorySection : trade_category_sections
        click TradeCategorySection href "../TradeCategorySection"
    

        
      TradeBusinessArea : trade_common_component_details
        
          
    
        
        
        TradeBusinessArea --> "*" TradeCommonComponentDetail : trade_common_component_details
        click TradeCommonComponentDetail href "../TradeCommonComponentDetail"
    

        
      TradeBusinessArea : trade_common_components
        
          
    
        
        
        TradeBusinessArea --> "*" TradeCommonComponentName : trade_common_components
        click TradeCommonComponentName href "../TradeCommonComponentName"
    

        
      TradeBusinessArea : trade_components_overview_note
        
      TradeBusinessArea : trade_diagram_conventions
        
      TradeBusinessArea : trade_footnotes
        
          
    
        
        
        TradeBusinessArea --> "*" TradeComponentTableFootnote : trade_footnotes
        click TradeComponentTableFootnote href "../TradeComponentTableFootnote"
    

        
      TradeBusinessArea : trade_introduction
        
      TradeBusinessArea : trade_message_diagram_template_url
        
      TradeBusinessArea : trade_messages_overview_note
        
      
```
