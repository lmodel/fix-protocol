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
  One of the five parts of FIX by business area, such as pre-trade or post-trade.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class FixSection extends FixElement {

  private String fixmlFileName;
  private Boolean fixmlNotRequired;
  private Integer sectionOrder;


}