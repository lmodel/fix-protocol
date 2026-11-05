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
  A group of messages within a section. Three categories sit in no section and hold the shared components and the fields instead.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class FixCategory extends FixElement {

  private String fixmlFileName;
  private FixSection inSection;
  private Boolean fixmlNotRequired;
  private String categoryKind;
  private String includeFile;


}