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
  When FIX added, last changed and deprecated an element, by version and extension pack.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class FixPedigreeMixin  {

  private String addedIn;
  private Integer addedInEp;
  private String updatedIn;
  private Integer updatedInEp;
  private String deprecatedIn;
  private Integer deprecatedInEp;


}