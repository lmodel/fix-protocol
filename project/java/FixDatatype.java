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
  A kind of value a field holds, such as int, Price or UTCTimestamp, with the XML Schema types it maps to.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class FixDatatype extends FixElement {

  private FixDatatype baseType;
  private List<FixMappedDatatype> mappedDatatypes;


}