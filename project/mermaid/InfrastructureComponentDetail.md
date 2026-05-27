


```mermaid
 classDiagram
    class InfrastructureComponentDetail
    click InfrastructureComponentDetail href "../InfrastructureComponentDetail"
      InfrastructureComponentDetail : component_name
        
      InfrastructureComponentDetail : description
        
      InfrastructureComponentDetail : infra_layout_rows
        
          
    
        
        
        InfrastructureComponentDetail --> "*" InfrastructureLayoutRow : infra_layout_rows
        click InfrastructureLayoutRow href "../InfrastructureLayoutRow"
    

        
      InfrastructureComponentDetail : layout_url
        
      InfrastructureComponentDetail : repetition
        
          
    
        
        
        InfrastructureComponentDetail --> "0..1" ComponentRepetition : repetition
        click ComponentRepetition href "../ComponentRepetition"
    

        
      
```
