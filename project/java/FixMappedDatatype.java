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
  The type of another standard that a FIX datatype takes, such as xs:decimal in XML Schema.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class FixMappedDatatype  {

  private String mappedStandard;
  private String mappedBase;
  private Boolean mappedBuiltin;
  private String mappedMinInclusive;
  private String mappedPattern;


}