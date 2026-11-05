package example;

/* metamodel_version: 1.12.0 */
/* version: FIX.Latest_EP312 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  One field, component or group in a message, component or group, and whether it must be there.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class FixMember  {

  private FixField memberField;
  private FixComponent memberComponent;
  private FixGroup memberGroup;
  private String presence;
  private Boolean fixmlInlined;
  private String addedIn;
  private Integer addedInEp;
  private String updatedIn;
  private Integer updatedInEp;
  private String deprecatedIn;
  private Integer deprecatedInEp;


}