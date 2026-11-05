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
  The field that counts a group's repeats, as the group names it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class FixNumInGroup  {

  private FixField countField;
  private String addedIn;
  private Integer addedInEp;
  private String updatedIn;
  private Integer updatedInEp;
  private String deprecatedIn;
  private Integer deprecatedInEp;


}