


```mermaid
 classDiagram
    class InfrastructureCategorySection
    click InfrastructureCategorySection href "../InfrastructureCategorySection"
      InfrastructureCategorySection : application_message_report_uses
        
          
    
        
        
        InfrastructureCategorySection --> "*" ApplicationMessageReportTypeEnum : application_message_report_uses
        click ApplicationMessageReportTypeEnum href "../ApplicationMessageReportTypeEnum"
    

        
      InfrastructureCategorySection : category
        
          
    
        
        
        InfrastructureCategorySection --> "1" InfrastructureCategoryEnum : category
        click InfrastructureCategoryEnum href "../InfrastructureCategoryEnum"
    

        
      InfrastructureCategorySection : category_components_note
        
      InfrastructureCategorySection : description
        
      InfrastructureCategorySection : infra_category_specific_components
        
          
    
        
        
        InfrastructureCategorySection --> "*" InfrastructureComponentDetail : infra_category_specific_components
        click InfrastructureComponentDetail href "../InfrastructureComponentDetail"
    

        
      InfrastructureCategorySection : messages
        
          
    
        
        
        InfrastructureCategorySection --> "*" InfrastructureMessageDetail : messages
        click InfrastructureMessageDetail href "../InfrastructureMessageDetail"
    

        
      InfrastructureCategorySection : network_request_types_referenced
        
          
    
        
        
        InfrastructureCategorySection --> "*" NetworkRequestTypeEnum : network_request_types_referenced
        click NetworkRequestTypeEnum href "../NetworkRequestTypeEnum"
    

        
      InfrastructureCategorySection : network_status_scenarios
        
          
    
        
        
        InfrastructureCategorySection --> "*" NetworkStatusScenarioEnum : network_status_scenarios
        click NetworkStatusScenarioEnum href "../NetworkStatusScenarioEnum"
    

        
      InfrastructureCategorySection : title
        
      
```
