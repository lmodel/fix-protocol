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
  An element of FIX Latest with an identifier and a name of its own.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class FixElement  {

  private URI id;
  private String name;
  private String addedIn;
  private Integer addedInEp;
  private String updatedIn;
  private Integer updatedInEp;
  private String deprecatedIn;
  private Integer deprecatedInEp;


}