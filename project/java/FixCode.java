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
  One value of a code set, with its name, such as 1 for Buy.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class FixCode extends FixElement {

  private String codeValue;
  private Integer sortOrder;
  private String codeGroup;


}