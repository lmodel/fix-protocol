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
  A named block of fields, components and groups that messages share, such as Instrument.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class FixComponent extends FixElement {

  private String abbrName;
  private FixCategory inCategory;
  private List<FixMember> fixMembers;
  private Boolean fixmlNotRequired;


}