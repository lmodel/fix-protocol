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
  A list of the values a field may take, each a code with a name, such as the sides of an order.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class FixCodeSet extends FixElement {

  private FixDatatype codeSetDatatype;
  private List<FixCode> fixCodes;


}