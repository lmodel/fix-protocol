


```mermaid
 classDiagram
    class InfrastructureMessageDetail
    click InfrastructureMessageDetail href "../InfrastructureMessageDetail"
      InfrastructureMessageDetail : description
        
      InfrastructureMessageDetail : infra_layout_rows
        
          
    
        
        
        InfrastructureMessageDetail --> "*" InfrastructureLayoutRow : infra_layout_rows
        click InfrastructureLayoutRow href "../InfrastructureLayoutRow"
    

        
      InfrastructureMessageDetail : layout_url
        
      InfrastructureMessageDetail : message_name
        
      InfrastructureMessageDetail : msg_type
        
      
```
