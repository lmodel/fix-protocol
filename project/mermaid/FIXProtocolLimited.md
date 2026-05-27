


```mermaid
 classDiagram
    class FIXProtocolLimited
    click FIXProtocolLimited href "../FIXProtocolLimited"
      FIXProtocolLimited : brand_name
        
      FIXProtocolLimited : committees_url
        
      FIXProtocolLimited : governance_bodies
        
          
    
        
        
        FIXProtocolLimited --> "*" FPLCommitteeRole : governance_bodies
        click FPLCommitteeRole href "../FPLCommitteeRole"
    

        
      FIXProtocolLimited : legal_name
        
      FIXProtocolLimited : member_firms_url
        
      FIXProtocolLimited : member_types
        
          
    
        
        
        FIXProtocolLimited --> "*" FPLMemberType : member_types
        click FPLMemberType href "../FPLMemberType"
    

        
      FIXProtocolLimited : product_committees
        
          
    
        
        
        FIXProtocolLimited --> "*" FPLProductGroup : product_committees
        click FPLProductGroup href "../FPLProductGroup"
    

        
      FIXProtocolLimited : regional_committees
        
          
    
        
        
        FIXProtocolLimited --> "*" FPLRegion : regional_committees
        click FPLRegion href "../FPLRegion"
    

        
      FIXProtocolLimited : website
        
      FIXProtocolLimited : working_groups_url
        
      
```
