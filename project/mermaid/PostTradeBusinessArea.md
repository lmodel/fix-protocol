


```mermaid
 classDiagram
    class PostTradeBusinessArea
    click PostTradeBusinessArea href "../PostTradeBusinessArea"
      PostTradeBusinessArea : area
        
          
    
        
        
        PostTradeBusinessArea --> "1" BusinessAreaEnum : area
        click BusinessAreaEnum href "../BusinessAreaEnum"
    

        
      PostTradeBusinessArea : components
        
          
    
        
        
        PostTradeBusinessArea --> "1..*" PostTradeComponentEntry : components
        click PostTradeComponentEntry href "../PostTradeComponentEntry"
    

        
      PostTradeBusinessArea : components_overview_note
        
      PostTradeBusinessArea : diagram_conventions
        
      PostTradeBusinessArea : messages
        
          
    
        
        
        PostTradeBusinessArea --> "1..*" PostTradeMessageEntry : messages
        click PostTradeMessageEntry href "../PostTradeMessageEntry"
    

        
      PostTradeBusinessArea : messages_overview_note
        
      PostTradeBusinessArea : post_category_sections
        
          
    
        
        
        PostTradeBusinessArea --> "*" PostTradeCategorySection : post_category_sections
        click PostTradeCategorySection href "../PostTradeCategorySection"
    

        
      PostTradeBusinessArea : post_common_component_details
        
          
    
        
        
        PostTradeBusinessArea --> "*" PostTradeCommonComponentDetail : post_common_component_details
        click PostTradeCommonComponentDetail href "../PostTradeCommonComponentDetail"
    

        
      PostTradeBusinessArea : post_common_components
        
          
    
        
        
        PostTradeBusinessArea --> "*" PostTradeCommonComponentName : post_common_components
        click PostTradeCommonComponentName href "../PostTradeCommonComponentName"
    

        
      PostTradeBusinessArea : post_footnotes
        
          
    
        
        
        PostTradeBusinessArea --> "*" PostTradeComponentTableFootnote : post_footnotes
        click PostTradeComponentTableFootnote href "../PostTradeComponentTableFootnote"
    

        
      PostTradeBusinessArea : post_introduction
        
      PostTradeBusinessArea : published_version
        
      PostTradeBusinessArea : publisher
        
      PostTradeBusinessArea : referenced_global_components
        
          
    
        
        
        PostTradeBusinessArea --> "*" GlobalComponent : referenced_global_components
        click GlobalComponent href "../GlobalComponent"
    

        
      PostTradeBusinessArea : title
        
      
```
