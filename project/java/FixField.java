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
  A field of FIX, known by its tag number, such as 55 for Symbol, with the datatype or code set of its values.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class FixField extends FixElement {

  private String abbrName;
  private Boolean fixmlNotRequired;
  private FixDatatype fieldDatatype;
  private FixCodeSet fieldCodeSet;
  private FixDatatype unionDatatype;
  private FixField lengthField;
  private FixField discriminatorField;
  private FixCategory baseCategory;
  private String baseCategoryAbbrName;


}